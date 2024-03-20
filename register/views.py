from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import RegisterForm, UpdateUserForm
from django.contrib.auth import login, logout
from django.views.generic import UpdateView


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


class ProfileEditView(UpdateView):
    template_name = "edit_profile.html"
    form_class = UserChangeForm
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user
