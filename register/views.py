from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import RegisterForm, UpdateProfileForm
from django.contrib.auth import login, logout
from django.views.generic import UpdateView, CreateView, ListView, DetailView

from .models import UserProfile


# Create your views here.

def logout_view(request):
    logout(request)
    return render(request, "home.html")


class CreateUserView(CreateView):
    template_name = "registration/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('home')


class ProfileEditView(UpdateView):
    template_name = "registration/edit_profile.html"
    fields = ["bio", "display_name", "profile_pic"]
    model = UserProfile
    # form_class = UpdateProfileForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileEditView, self).get_context_data()
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

    def get_object(self, queryset=None):
        return self.request.user


class ProfileView(DetailView):
    model = UserProfile
    template_name = "registration/profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data()
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

    def get_object(self, queryset=None):
        return self.request.user
