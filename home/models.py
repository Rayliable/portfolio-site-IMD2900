import sys
from PIL.Image import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from io import BytesIO
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
        ('option_five', 'Animation'),
        ('option_six', '3D'),
        ('option_seven', 'Painting'),
    ]

    OPTIONS2 = [  # privacy options
        (public, 'Public'),
        ('option_two', 'Private')
    ]

    title = models.CharField(max_length=255)
    image_upload = models.ImageField(upload_to='user_upload/full_quality/')
    image_compressed = models.ImageField(upload_to='user_upload/compressed', blank=True)
    tags = models.CharField(max_length=30, choices=OPTIONS, default=untagged)
    privacy = models.CharField(max_length=30, choices=OPTIONS2, default=public)

    # code modified off of Rowan's code from BIT2008 and
    # code for saving into model modified from
    # https://stackoverflow.com/questions/67244002/how-to-create-inmemoryuploadedfile-objects-proper-in-django
    def save(self, *args, **kwargs):
        if self.image_upload:
            # Open the full-quality image
            img = Image.open(self.image_upload)
            output_io = BytesIO()

            # Resize and save the compressed image
            img.thumbnail((800, 800))
            img.save(output_io, format='JPEG', quality=60)  # Save with 60% quality
            output_io.seek(0)

            # Save the compressed image to the compressed_image field
            self.image_compressed = InMemoryUploadedFile(
                output_io,
                'ImageField', '{}.jpg'.format(self.image_upload.name.split('.')[0]),
                'image/jpeg',
                sys.getsizeof(output_io),
                None
            )

        super(UserUpload, self).save(*args, **kwargs)

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
        ('option_five', 'Animation'),
        ('option_six', '3D'),
        ('option_seven', 'Painting'),
    ]

    OPTIONS2 = [  # privacy options
        (public, 'Public'),
        ('option_two', 'Private')
    ]

    title = models.CharField(max_length=255)
    url_upload = models.URLField()
    tags = models.CharField(max_length=30, choices=OPTIONS, default=untagged)
    privacy = models.CharField(max_length=30, choices=OPTIONS2, default=public)

    # uploader = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
