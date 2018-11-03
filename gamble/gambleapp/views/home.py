import zipfile
import os

from django.views.generic import CreateView
from django.shortcuts import reverse, redirect

from gambleapp.models import Accusation, AccusationImage


class HomeView(CreateView):
    template_name = 'gambleapp/home.html'
    model = Accusation
    fields = ['url', 'site_id', 'password']

    def form_valid(self, form):
        result = super().form_valid(form)
        images = ['/Users/hanminsoo/Desktop/github/judge_gamble/gamble/gamble/media/0.jpg']

        jungle_zip = zipfile.ZipFile('/Users/hanminsoo/Desktop/github/judge_gamble/gamble/gamble/media/image.zip','w')
        for folder, subfolders, files in os.walk('/Users/hanminsoo/Desktop/github/judge_gamble/gamble/gamble/media/image'):
            for file in files:
                jungle_zip.write(os.path.join(folder, file),compress_type=zipfile.ZIP_DEFLATED)
            pass
        # jungle_zip.write('/Users/hanminsoo/Desktop/github/judge_gamble/gamble/gamble/media/0.jpg', compress_type=zipfile.ZIP_DEFLATED)
        jungle_zip.close()
        return result

    def form_invalid(self, form):
        return redirect(reverse('home'))
