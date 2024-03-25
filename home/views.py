from django.contrib import messages
from django.shortcuts import render, redirect
import os, csv
from portfolio_site_IMD2900.settings import BASE_DIR
from .forms import ImageForm, ImageFormURL, ContactForm
from .models import UserUpload, UserUploadURL


# Create your views here.


def home(request):  # home page of site
    return render(request, "home.html")


def about(request):  # about page of site
    return render(request, "about.html")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Do something here!!!!
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            file_path = os.path.join(BASE_DIR, 'responses.csv')
            f = open(file_path, "a")
            writer = csv.writer(f)
            writer.writerow([name, email, subject, message])
            f.close()

            messages.success(request, f'Thank you for your message, {name}!')
            return redirect('contact_us')
        else:
            messages.warning(request, f"Sorry, something about that wasn't right. Please try again.")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


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


def graphic_design(request):
    # Filter through images based on tag and privacy
    filtered_images = UserUpload.objects.filter(tags='option_four', privacy='option_one')
    filtered_images_url = UserUploadURL.objects.filter(tags='option_two', privacy='option_one')
    return render(request, 'graphicDesign.html', {'images': filtered_images, 'url_images': filtered_images_url})


def animation(request):
    # Filter through images based on tag and privacy
    filtered_images = UserUpload.objects.filter(tags='option_five', privacy='option_one')
    filtered_images_url = UserUploadURL.objects.filter(tags='option_two', privacy='option_one')
    return render(request, 'animation.html', {'images': filtered_images, 'url_images': filtered_images_url})


def threedee(request):
    # Filter through images based on tag and privacy
    filtered_images = UserUpload.objects.filter(tags='option_six', privacy='option_one')
    filtered_images_url = UserUploadURL.objects.filter(tags='option_two', privacy='option_one')
    return render(request, '3d.html', {'images': filtered_images, 'url_images': filtered_images_url})


def painting(request):
    # Filter through images based on tag and privacy
    filtered_images = UserUpload.objects.filter(tags='option_seven', privacy='option_one')
    filtered_images_url = UserUploadURL.objects.filter(tags='option_two', privacy='option_one')
    return render(request, 'painting.html', {'images': filtered_images, 'url_images': filtered_images_url})


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
