from django import forms
from api.models import COUNTRY_CHOICES

# Form fields reference at docs.djangoproject.com/en/2.2/ref/forms/fields/

# Used to validate Person model. Doesn't come from an actual form
class PersonForm(forms.Form):
    # By default, each Field class assumes the value is required, so if you pass an empty value - either None or the empty string ("") - then clean() wil raise a ValidationError exception.

    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    # email: "" in json body will fail
    email = forms.EmailField(max_length=50)
    birth_date = forms.DateField(required=False)
    # do a custom form validation to make sure country is in COUNTRY_CHOICES
    country = forms.CharField(required=False, max_length=100)

# You can write code to perform validation for particular form fields (based on their name) or for the form as a whole (considering combinations of various fields)

    # docs.djangoproject.com/en/2.2/ref/forms/validation
    def clean_email(self):
        print("cleaning email")
        # because the general field clean() method has already cleaned the data once
        print(self.cleaned_data["email"])