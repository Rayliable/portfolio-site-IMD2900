from django.shortcuts import render, redirect
from .forms import ImageForm, ImageFormURL
from .models import UserUpload, UserUploadURL


# Create your views here.


def home(request):  # home page of site
    return render(request, "home.html")


def about(request):  # about page of site
    return render(request, "about.html")


def contact(request):  # contact page of site
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


def photography(request):
    # Filter through images based on tag and privacy
    filtered_images = UserUpload.objects.filter(tags='option_two', privacy='option_one')
    filtered_images_url = UserUploadURL.objects.filter(tags='option_two', privacy='option_one')
    return render(request, 'photography.html', {'images': filtered_images, 'url_images': filtered_images_url})


def illustration(request):
    # Filter through images based on tag and privacy
    filtered_images = UserUpload.objects.filter(tags='option_three', privacy='option_one')
    filtered_images_url = UserUploadURL.objects.filter(tags='option_two', privacy='option_one')
    return render(request, 'illustration.html', {'images': filtered_images, 'url_images': filtered_images_url})

def accpieces_view(request):  # home page of site
    return render(request, "acc-viewpieces.html")


def viewart_view(request):  # home page of site
    return render(request, "ViewArtPage.html")


def extra_view(request):  # home page of site
    return render(request, "Extra.html")


def detail_view(request):  # home page of site
    return render(request, "detail.html")


def SignIn_view(request):  # home page of site
    return render(request, "register/SignIn.html")
