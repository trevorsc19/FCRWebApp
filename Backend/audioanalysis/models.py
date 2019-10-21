from django.db import models

# Create your models here.
class Audio(models.Model):
    audio = models.FileField(upload_to='audio/')