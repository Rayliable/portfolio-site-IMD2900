from django.contrib import admin
from .models import UserUpload, UserUploadURL

# Register your models here.
admin.site.register(UserUpload)
admin.site.register(UserUploadURL)
