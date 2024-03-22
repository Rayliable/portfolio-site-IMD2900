from django.contrib import admin
from .models import UserUpload, UserUploadURL
from register.models import Profile

# Register your models here.
admin.site.register(UserUpload)
admin.site.register(UserUploadURL)
# admin.site.register(Profile)
