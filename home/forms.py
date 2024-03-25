from io import BytesIO
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.sites import requests
from django.core.validators import EmailValidator

from .models import UserUpload, UserUploadURL
from PIL import Image
import requests


class ImageForm(forms.ModelForm):  # upload form for file image

    class Meta:
        model = UserUpload
        fields = ['title', 'image_upload', 'tags', 'privacy']


class ImageFormURL(forms.ModelForm):  # upload form for URL image
    class Meta:
        model = UserUploadURL
        fields = ['title', 'url_upload', 'tags', 'privacy']


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True, validators=[EmailValidator()])
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, required=True)
