from django.db import models

# Create your models here.
class Audio(models.Model):
    # If you are using the default FileSystemStorage, the string value will be appended to your MEDIA_ROOT path to form the location on the local filesystem where uploaded files will be stored
    name = models.CharField(max_length=128)
    audio_file = models.FileField(upload_to='audio/', blank=False, null=True)
    s3_url = models.URLField(max_length=500, default="RANDOM TEXT")