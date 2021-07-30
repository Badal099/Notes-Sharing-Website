from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from NotesApp.models import *
from UserApp.models import *
from AdminApp.models import *
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def userlogin(request):
    error = ""
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        try:
            if user:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'userlogin.html',d)

def adminlogin(request):
    error = ""
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'adminlogin.html',d)

def signup1(request):
    error = ""
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']
        branch = request.POST['branch']
        role = request.POST['role']
        try:
            user = User.objects.create_user(username=email,password=password,first_name=fname,last_name=lname)
            Signup.objects.create(user=user,contact=contact,branch=branch,role=role)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'signup.html', d)