from django.db import models
#from django.contrib.auth.models import User
from users.models import CustomUser
from django.contrib.auth.models import AbstractUser

# pip install pycountry (once activating virtual environment)
import pycountry

#https://medium.com/better-programming/list-comprehension-in-python-8895a785550b
COUNTRY_CHOICES = [n.name for n in pycountry.countries]
import audioanalysis.models
# By default, Django will create a table profile_profile
# Models fields reference: https://docs.djangoproject.com/en/2.2/ref/models/fields/
class Profile(models.Model):
    # adds a user_id column to the table
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE, 
        null=True
    )
    # many to one relationship. Multiple audio entries to one Profile. Django appends "_id" to the field name to its database column name
    audio_file = models.ForeignKey(audioanalysis.models.Audio, on_delete=models.CASCADE, null=True)
    # we could also use now() postgres function
    account_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    first_name = models.CharField(null=True, max_length=30)
    last_name = models.CharField(null=True, max_length=30)
    email = models.EmailField(null=False, default=None, max_length=50, unique=True)
    # argument set to false by default
    birth_date = models.DateField(null=True)
    country = models.CharField(null=True, default=None, max_length=100)

    class Meta:
        db_table = "profile_table"
    
    # This runs when printing a Person object
    def __str__(self):
        return "user: {} first_name: {} last_name: {} email: {} birth_date: {} country: {}".format(self.user.get_username(),self.first_name, self.last_name, self.email, self.birth_date, self.country)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Image(models.Model):
    picture = models.ImageField(upload_to='images/')