from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("image_upload/", views.image_upload, name="image_upload"),
    path("url_upload/", views.url_upload, name="url_upload"),
    path("upload_view/", views.upload_view, name="upload_view"),
    path("about_us/", views.about, name="about_us"),
    path("contact_us", views.contact, name="contact_us"),
    path("photography/", views.photography, name="photography"),
    path("illustration/", views.illustration, name="illustration"),
]
