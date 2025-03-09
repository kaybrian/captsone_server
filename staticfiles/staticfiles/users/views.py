from django.shortcuts import render
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required(login_url="/users/login/")
def addUser(request):
    context={
        "title": "Add User",
        "subTitle": "Add User",
    }
    return render(request, "users/addUser.html", context)


@login_required(login_url="/users/login/")
def usersGrid(request):
    context={
        "title": "Users Grid",
        "subTitle": "Users Grid",
    }
    return render(request, "users/usersGrid.html", context)

@login_required(login_url="/users/login/")
def usersList(request):
    context={
        "title": "Users List",
        "subTitle": "Users List",
    }
    return render(request, "users/usersList.html", context)


@login_required(login_url="/users/login/")
def viewProfile(request):
    context={
        "title": "View Profile",
        "subTitle": "View Profile",
    }
    return render(request, "users/viewProfile.html", context)

def login(request):
    context={
        "title": "Login",
        "subTitle": "Login",
    }
    return render(request, "authentication/signin.html", context)