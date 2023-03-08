from django.shortcuts import render
from django.conf import settings

from datetime import datetime
import os

today = datetime.now()
FILE_DIR = os.path.join(settings.MEDIA_ROOT, 'documents')


def handle_uploaded_file(f):
    with open(os.path.join(FILE_DIR, f'{today.strftime("%Y-%m-%d")}_{f.name}'), 
              'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def xml_uploader(request):
    pass
