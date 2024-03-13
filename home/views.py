from django.shortcuts import render, redirect
from .forms import ImageForm, ImageFormURL


# Create your views here.


def home(request):  # home page of site
    return render(request, "home.html")


def about(request):  # home page of site
    return render(request, "about.html")


def contact(request):  # home page of site
    return render(request, "contact.html")


def upload_view(request):  # view for the upload form
    form = ImageForm
    form2 = ImageFormURL
    return render(request, 'upload.html', {'form': form, 'form2': form2})


def image_upload(request):  # page for users to upload images
    if request.method == 'POST':
        print(request.FILES)
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid:  # if form one was valid
            form.save()
        else:  # if invalid print errors
            form = ImageForm()
            form2 = ImageFormURL()
    return redirect("upload_view")  # return to form view


def url_upload(request):  # page for users to upload images
    if request.method == 'POST':
        print(request.FILES)
        form = ImageFormURL(request.POST)
        if form.is_valid:  # if form one was valid
            form.save()
        else:  # if invalid print errors
            form = ImageForm()
    return redirect("upload_view")  # return to form view
