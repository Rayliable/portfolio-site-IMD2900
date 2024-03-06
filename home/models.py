from django.db import models


# Create your models here.

# user uploads mode (includes title, image, tags (not implemented yet))
class UserUpload(models.Model):
    untagged = 'option_one'
    public = 'option_one'

    OPTIONS = [
        (untagged, 'untagged'),
        ('option_two', 'Photography'),
        ('option_three', 'Illustration'),
        ('option_four', 'Graphic Design'),
    ]

    OPTIONS2 = [
        (public, 'Public'),
        ('option_two', 'Private')
    ]

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='user_upload/')
    tags = models.CharField(max_length=30, choices=OPTIONS, default=untagged)
    privacy = models.CharField(max_length=30, choices=OPTIONS2, default=public)

    def __str__(self):
        return self.title
