from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from UserApp.views import *

urlpatterns = [
    path('',userhome,name='userhome'),
    path('profile/',profile,name='profile'),
    path('editprofile/',editprofile,name='editprofile'),
    path('uploadnotes/',uploadnotes,name='uploadnotes'),
    path('viewmynotes/',viewmynotes,name='viewmynotes'),
    path('viewallnotes/',viewallnotes,name='viewallnotes'),
    path('deletemynotes/<int:pid>',deletemynotes,name='deletemynotes'),
    path('changepassword/',changepassword,name='changepassword'),
    path('userlogout/',userlogout,name='userlogout'),

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
