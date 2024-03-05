from django.shortcuts import render, redirect
from .forms import ImageForm


# Create your views here.


def home(request):  # home page of site
    return render(request, "home.html")


def about(request):  # home page of site
    return render(request, "about.html")


def contact(request):  # home page of site
    return render(request, "contact.html")


def upload_view(request):  # view for the upload form
    form = ImageForm
    return render(request, 'upload.html', {'form': form})


def image_upload(request):  # page for users to upload images
    if request.method == 'POST':
        print(request.FILES)
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid:  # if valid save to database
            form.save()
        else:  # if invalid print errors
            print(form.errors)
    return redirect("upload_view")  # return to form view
