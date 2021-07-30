from django.shortcuts import render,redirect
from NotesApp.models import *
from UserApp.models import *
from AdminApp.models import *
from django.contrib.auth import logout

# Create your views here.
def adminhome(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    pn = Notes.objects.filter(status="Pending").count()
    an = Notes.objects.filter(status="Accept").count()
    rn = Notes.objects.filter(status="Reject").count()
    alln = Notes.objects.all().count()
    d = {'pn':pn, 'an':an,'rn':rn,'alln':alln}
    return render(request, 'adminhome.html', d)

def viewuser(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    users = Signup.objects.all()
    d = {'users':users}
    return render(request, 'viewuser.html',d)

def viewnotes(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    return render(request, 'viewnotes.html')

def adminlogout(request):
    logout(request)
    return redirect('adminlogin')


def pending(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    notes = Notes.objects.filter(status="Pending")
    d = {'notes':notes}
    return render(request, 'pending.html',d)


def rejected(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    notes = Notes.objects.filter(status="Reject")
    d = {'notes':notes}
    return render(request, 'rejected.html',d)


def accepted(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    notes = Notes.objects.filter(status="Accept")
    d = {'notes':notes}
    return render(request, 'accepted.html',d)


def allnotes(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    notes = Notes.objects.all()
    d = {'notes':notes}
    return render(request, 'allnotes.html',d)

def deleteuser(request,pid):
    if not request.user.is_staff:
        return redirect('adminlogin')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('viewuser')

def delete_notes(request,pid):
    if not request.user.is_staff:
        return redirect('adminlogin')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('allnotes')

def assignstatus(request,pid):
    if not request.user.is_staff:
        return redirect('adminlogin')
    notes = Notes.objects.get(id=pid)
    error=""
    if request.method=="POST":
        s = request.POST['status']
        try:
            notes.status = s
            notes.save()
            error="no"
        except:
            error="yes"
    d = {'notes':notes,'error':error}
    return render(request, 'assignstatus.html',d)