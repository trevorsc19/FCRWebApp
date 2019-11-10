from django.contrib import admin
from profile import models

# Register your models here.

# This allows us to edit the models in the browser panel
admin.site.register(models.Profile)

admin.site.register(models.Image)