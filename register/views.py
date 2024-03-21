from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import RegisterForm, UpdateProfileForm
from django.contrib.auth import login, logout
from django.views.generic import UpdateView, CreateView, ListView


# Create your views here.

def logout_view(request):
    logout(request)
    return render(request, "home.html")


class CreateUserView(CreateView):
    template_name = "registration/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('home')


class ProfileEditView(UpdateView):
    template_name = "edit_profile.html"
    form_class = UpdateProfileForm
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user
