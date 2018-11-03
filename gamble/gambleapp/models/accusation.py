from django.db import models
from django.shortcuts import reverse


class Accusation(models.Model):

    url = models.CharField(max_length=255)
    site_id = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('home')