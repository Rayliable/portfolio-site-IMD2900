from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("image_upload/", views.image_upload, name="image_upload"),
    path("upload_view/", views.upload_view, name="upload_view"),
]