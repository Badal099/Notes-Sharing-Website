from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from NotesApp.views import *

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('userlogin/',userlogin,name='userlogin'),
    path('adminlogin/',adminlogin,name='adminlogin'),
    path('signup/',signup1,name='signup'),
    path('adminapp/',include('AdminApp.urls')),
    path('user/',include('UserApp.urls')),

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
