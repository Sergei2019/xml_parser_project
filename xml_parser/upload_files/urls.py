from django.urls import path

from . import views

app_name = 'upload_files'

urlpatterns = [
    path('list', views.xml_uploader, name='xml_uploader')

]