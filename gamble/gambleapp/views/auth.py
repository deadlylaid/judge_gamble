from django.views.generic import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout, get_user_model


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'gambleapp/login.html',
            {}
        )

    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        user = authenticate(
            username=username,
            password=password
        )
        if user:
            login(request, user)

        return redirect(reverse('home'))


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('home'))


class JoinUs(View):

    def get(self, request):
        return render(
            request,
            'gambleapp/joinus.html',
            {}
        )

    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        password2 = self.request.POST.get('password2')
        name = self.request.POST.get('name')
        phonenumber =self.request.POST.get('phonenumber')

        if password == password2:
            user = get_user_model().objects.create_user(
                username=username,
                password=password,
                name=name,
                phonenumber=phonenumber
            )
        else:
            return redirect(reverse('joinus'))
        login(request, user)
        return redirect(reverse('home'))
