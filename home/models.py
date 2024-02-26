from django.db import models


# Create your models here.

# user uploads mode (includes title, image, tags (not implemented yet))
class UserUpload(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='user_upload/')

    def __str__(self):
        return self.title
