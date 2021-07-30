from django.shortcuts import render,redirect
from NotesApp.models import *
from UserApp.models import *
from AdminApp.models import *
from django.contrib.auth import logout
from datetime import date

# Create your views here.
def userhome(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    return render(request, 'userhome.html')

def uploadnotes(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error = ""
    if request.method=="POST":
        b = request.POST['branch']
        s = request.POST['subject']
        n = request.FILES['notesfile']
        f = request.POST['filetype']
        d = request.POST['description']
        u = User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user=u,uploadingdate=date.today(),branch=b,subject=s,notesfile=n,filetype=f,description=d,status='Pending')
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'uploadnotes.html', d)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    d = {'data':data,'user':user}
    return render(request, 'profile.html',d)

def editprofile(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    error = ""
    if request.method=="POST":
        f = request.POST['firstname']
        l = request.POST['lastname']
        c = request.POST['contact']
        b = request.POST['branch']
        r = request.POST['role']
        user.first_name = f
        user.last_name = l
        data.contact = c
        data.branch = b
        data.role = r
        user.save()
        data.save()
        error = True
    d = {'data':data,'user':user,'error':error}
    return render(request, 'editprofile.html',d)

def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error = ""
    if request.method=="POST":
        old = request.POST['old']
        new = request.POST['new']
        confirm = request.POST['confirm']
        if new==confirm:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(new)
            u.save()
            error = "no"
        else:
            error = "yes"
    d = {'error':error}
    return render(request, 'changepassword.html',d)

def userlogout(request):
    logout(request)
    return redirect('userlogin')

def viewmynotes(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.filter(user=user)
    d = {'notes':notes}
    return render(request, 'viewmynotes.html',d)

def deletemynotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('viewmynotes')


def viewallnotes(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    notes = Notes.objects.filter(status='Accept')
    d = {'notes':notes}
    return render(request, 'viewallnotes.html', d)