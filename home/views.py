from django.shortcuts import render, redirect
from .forms import ImageForm
# Create your views here.


def home(request):  # home page of site
    return render(request, "home.html")


def image_upload(request):  # page for users to upload images
    if request.method == "POST":
        return render(request, "upload.html")
    else:
        return render(request, "upload.html")

