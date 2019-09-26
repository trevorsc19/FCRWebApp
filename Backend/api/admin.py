from django.contrib import admin
from api import models

# Register your models here.

# This allows us to edit the models in the browser panel
admin.site.register(models.Person)