from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("image_upload/", views.image_upload, name="image_upload"),
    path("url_upload/", views.url_upload, name="url_upload"),
    path("upload_view/", views.upload_view, name="upload_view"),
    path("about_us/", views.about, name="about_us"),
    path("contact_us/", views.contact, name="contact_us"),
    path("photography/", views.photography, name="photography"),
    path("illustration/", views.illustration, name="illustration"),
    path("accpieces_view/", views.accpieces_view, name="accpieces_view"),
    path("viewart_view/", views.viewart_view, name="viewart_view"),
    path("extra_view/", views.extra_view, name="extra_view"),
    path("detail_view/", views.detail_view, name="detail_view"),
    path("SignIn/", views.SignIn_view, name="SignIn_view"),
    path("graphic_design/", views.graphic_design, name="graphic_design"),
    path("3d/", views.threedee, name="3d"),
    path("animation/", views.animation, name="animation"),
    path("painting/", views.painting, name="painting"),
]
