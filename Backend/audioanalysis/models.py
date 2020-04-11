from django.db import models

# Create your models here.
class Audio(models.Model):
    # Upload to MEDIA_ROOT/audio/
    #audio = models.FileField(upload_to='audio/')
    s3_url = models.URLField(max_length=500, default="RANDOM TEXT")