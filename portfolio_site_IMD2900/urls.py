from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from register import views as regv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('register/', regv.register, name="register"),
    path('edit_profile/', regv.ProfileEditView.as_view(), name="edit_profile"),
    path('logout/', regv.logout_view, name="logout"),
    path('', include("django.contrib.auth.urls")),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

