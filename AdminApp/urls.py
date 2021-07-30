from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from AdminApp.views import *

urlpatterns = [
    path('',adminhome,name='adminhome'),
    path('viewuser/',viewuser,name='viewuser'),
    path('viewnotes/',viewnotes,name='viewnotes'),
    path('adminlogout/',adminlogout,name='adminlogout'),
    path('pending/',pending,name='pending'),
    path('rejected/',rejected,name='rejected'),
    path('accepted/',accepted,name='accepted'),
    path('allnotes/',allnotes,name='allnotes'),
    path('assignstatus/<int:pid>',assignstatus,name='assignstatus'),
    path('deleteuser/<int:pid>',deleteuser,name='deleteuser'),
    path('delete_notes/<int:pid>',delete_notes,name='delete_notes'),
    
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

