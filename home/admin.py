from django.contrib import admin
from .models import UserUpload, UserUploadURL, UserProfile

# Register your models here.
admin.site.register(UserUpload)
admin.site.register(UserUploadURL)
admin.site.register(UserProfile)
