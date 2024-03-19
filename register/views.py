from django.shortcuts import render, redirect
from .forms import RegisterForm, UpdateUserForm
from django.contrib.auth import login, logout


# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "registration/register.html", {"form": form})


def logout_view(request):
    logout(request)
    return render(request, "home.html")


def update_profile(response):
    if response.method == "POST":
        form = UpdateUserForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = UpdateUserForm()
    return render(response, "registration/edit_profile.html", {"form": form})

