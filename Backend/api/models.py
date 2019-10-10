from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# pip install pycountry (once activating virtual environment)
import pycountry

#https://medium.com/better-programming/list-comprehension-in-python-8895a785550b
COUNTRY_CHOICES = [n.name for n in pycountry.countries]

# By default, Django will create a table api_person
# Models fields reference: https://docs.djangoproject.com/en/2.2/ref/models/fields/
class Person(models.Model):
    # adds a user_id column to the table
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        null=True
    )
    # we could also use now() postgres function
    account_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    first_name = models.CharField(null=True, max_length=30)
    last_name = models.CharField(null=True, max_length=30)
    email = models.EmailField(null=False, default=None, max_length=50)
    # argument set to false by default
    birth_date = models.DateField(null=True)
    country = models.CharField(null=True, default=None, max_length=100)

    class Meta:
        db_table = "PERSON_TABLE"
    
    # This runs when printing a Person object
    def __str__(self):
        return "first_name: {} last_name: {} email: {} birth_date: {} country: {}".format(self.first_name, self.last_name, self.email, self.birth_date, self.country)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Image(models.Model):
    profile_picture = models.ImageField(upload_to='images/')