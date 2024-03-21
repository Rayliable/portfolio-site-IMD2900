from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# user uploads mode (includes title, image, tags)
class UserUpload(models.Model):
    untagged = 'option_one'
    public = 'option_one'

    OPTIONS = [  # tag options
        (untagged, 'untagged'),
        ('option_two', 'Photography'),
        ('option_three', 'Illustration'),
        ('option_four', 'Graphic Design'),
    ]

    OPTIONS2 = [  # privacy options
        (public, 'Public'),
        ('option_two', 'Private')
    ]

    title = models.CharField(max_length=255)
    image_upload = models.ImageField(upload_to='user_upload/')
    tags = models.CharField(max_length=30, choices=OPTIONS, default=untagged)
    privacy = models.CharField(max_length=30, choices=OPTIONS2, default=public)

    def __str__(self):
        return self.title


class UserUploadURL(models.Model):  # user upload for URL images
    untagged = 'option_one'
    public = 'option_one'

    OPTIONS = [  # tag options
        (untagged, 'untagged'),
        ('option_two', 'Photography'),
        ('option_three', 'Illustration'),
        ('option_four', 'Graphic Design'),
    ]

    OPTIONS2 = [  # privacy options
        (public, 'Public'),
        ('option_two', 'Private')
    ]

    title = models.CharField(max_length=255)
    url_upload = models.URLField()
    tags = models.CharField(max_length=30, choices=OPTIONS, default=untagged)
    privacy = models.CharField(max_length=30, choices=OPTIONS2, default=public)

    def __str__(self):
        return self.title


# extends user model for pfp, display name, etc.
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    display_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='user_upload/pfp/', blank=True, null=True)

    def __str__(self):
        return 'User: '+str(self.user)
