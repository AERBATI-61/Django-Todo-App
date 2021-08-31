from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import *

def loginuser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

# authenticate -> boyle bir kullanici database de var mi yok mu kontrol ediyor
        user = authenticate(username = username, password = password)
        if user is None:
            messages.info(request, "Boyle Bir kullanici Bulunmamaktadir")
            return render(request, 'login.html', context)
        else:
            messages.success(request, " Basariyla Gris Yaptiniz")
            login(request, user)
            return redirect('index')
    return render(request, 'login.html', context)


def logoutuser(request):
    logout(request)
    messages.success(request, "Basariyla Cikis Yaptiniz")
    return redirect('index')


# def registerview(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#
#             newUser = User(username=username)
#             newUser.set_password(password)
#             newUser.save()
#             login(request, newUser)
#             return redirect('index')
#
#         context = {
#             "form": form
#         }
#         return render(request, 'register.html', context)
#
#
#     else:
#         form = RegisterForm()
#         context = {
#             "form": form
#         }
#         return render(request, 'register.html', context)


def registeruser(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.info(request, "Basariyla kayit oldunuz")
        return redirect('index')

    context = {
        "form": form
    }
    return render(request, 'register.html', context)
