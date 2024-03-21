from django.contrib.auth.models import User
from django.db import models


# Create your models here.


# extends user model for pfp, display name, etc.
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='user_upload/pfp/', blank=True, null=True)

    def __str__(self):
        return 'Profile: ' + str(self.user)
