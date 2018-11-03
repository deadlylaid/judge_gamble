from django.views.generic import CreateView
from django.shortcuts import reverse, redirect

from gambleapp.models import Accusation


class HomeView(CreateView):
    template_name = 'gambleapp/home.html'
    model = Accusation
    fields = ['url', 'site_id', 'password']

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect(reverse('home'))