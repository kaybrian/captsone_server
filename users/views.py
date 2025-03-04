from django.shortcuts import render
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from patient.models import Patient, HealthVital



@login_required()
def addUser(request):
    
    context={
        "title": "Add User",
        "subTitle": "Add User",
    }
    return render(request, "users/addUser.html", context)


@login_required()
def usersGrid(request):
    context={
        "title": "Users Grid",
        "subTitle": "Users Grid",
    }
    return render(request, "users/usersGrid.html", context)

@login_required()
def usersList(request):
    patients = Patient.objects.all()
    
    # add the patient to the context 
    context={
        "title": "Users List",
        "subTitle": "Users List",
        "patients": patients,
    }
    return render(request, "users/usersList.html", context)


@login_required()
def viewProfile(request):
    context={
        "title": "View Profile",
        "subTitle": "View Profile",
    }
    return render(request, "users/viewProfile.html", context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/users/login')
    context={
        "title": "Login",
        "subTitle": "Login",
    }

    return render(request, "authentication/signin.html", context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/users/login')