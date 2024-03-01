from django import forms
from .models import UserUpload


class ImageForm(forms.ModelForm):
    class Meta:
        model = UserUpload
        fields = ['title', 'image', 'tags']
