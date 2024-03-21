from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from home.models import UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UpdateProfileForm(UserChangeForm):
    email = forms.EmailField(required=False)
    username = forms.CharField(max_length=150, required=False)
    display_name = forms.CharField(max_length=255, required=False)
    password = forms.CharField(widget=forms.PasswordInput, max_length=250, required=False)
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ["username", "email", "display_name", "password", "profile_pic"]
