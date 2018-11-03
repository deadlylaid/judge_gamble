from django.views.generic import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout


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
            username = username,
            password = password
        )
        if user:
            login(request, user)

        return redirect(reverse('home'))


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('home'))