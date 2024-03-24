from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from register import views as regv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('', include("register.urls")),
    path('', include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # hey dan, just wanted to make it easier to change for deployment :)
