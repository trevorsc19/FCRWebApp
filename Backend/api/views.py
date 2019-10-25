from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views import View
from api import models
import json 
from api import status
from django.http import Http404
from django.db import connection
from django.core import serializers
from api import forms

def my_custom_sql():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM \"PERSON_TABLE\";")
        row = cursor.fetchone()
        #cusor.execute("TRUNCATE \"PERSON_TABLE\";")
        #cusor.execute("DELETE FROM \"PERSON_TABLE\";")
        print(row)
    return row

"""
can also do 
class DeleteTable(View):
    get(self, requeset):
        .....
"""
def delete_table(request):

    if request.method == 'GET':
        my_custom_sql()
        text = """<h1>Table Deleted</h1>"""
        return HttpResponse(text)

        #return JsonResponse({'response':"table successfully deleted"})

"""
docs.djangoproject.com/en/2.2/ref/models/querysets/ - QuerySets API reference
"""

"""

Below is from docs.djangoproject.com/en/2.2/topics/http/urls

How Django processes a request:

    1. Django determines the root URLconf module to use. Ordinarily, this is the value of the ROOT_URLCONF setting

    2. Django loads that Python module and looks for the variable urlpatterns. This should be a sequence of django.urls.path() and/or django.urls.re_path() instances

    3. Django runs through each URL pattern, in order, and stops at the first one that marches the requested URL

    4. Once one of the URL patterns matches, Django imports and calls the given view, which is a simple Python function (or a class-vased view). The view gets passed the following arguments:
        - An instance of HttpRequest
        - If the matched URL pattern returned no named groups, then the matches from the regular expression are provided as positional arguments.
        - The keyword arguments are made up of any named parts matched by the path expression, overriden by any arguments specified in the optional kwargs argument to django.urls.path() or django.urls.re_path()
    5. If no URL pattern matches, or if an exception is raised uring any point in this process, Django invokes and appropriate error-handling view. 

Below is from docs.djangoproject.com/en/2.2/ref/class-based-views/base/

class django.views.generic.base.View - The master class-based view. All other class-based views inherit from this base class.

Method Flowchart
    1.  setup()
    2.  dispatch()
    3.  http_method_not_allowed()
    4.  options()

"""

# Create your views here.

# docs.djangoproject.com/en/2.2/ref/class-based-views/
# list of HTTP method names this view will accept ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

# List all people, filter people, or create a new person
class PersonList(View):
    def get(self, request, *args, **kwargs):
        # docs.djangoproject/en/2.2/refs/models/querysets
        # returns a QuerySet that returns dictionaries, rather than model instances
        queryset = models.Person.objects.all().values()
        query_params = request.GET
        print(query_params)
        # request.GET['first_name'] will return MultiValueDictKeyError if it can't find first_name
        firstname_param = request.GET.get('first_name', None)
        country_param = request.GET.get('country', None)
        if request.GET.get('first_name') is not None:
            print("first name query parameter found")
            queryset = queryset.filter(first_name__iexact=firstname_param)
        if request.GET.get('country') is not None:
            print("country parameter found")
            queryset = queryset.filter(country__iexact=country_param)
        
        # An HttpResponse subclass that helps to create a JSON-encoded response
        return JsonResponse({'results': list(queryset)}, status=status.Code.HTTP_200_OK)
        #return HttpResponseBadRequest()

    # create person object. Validate the person. If correct, save. If not return error
    def post(self, request, *args, **kwargs):
        import json

        print("POST request")
        # decode the binary data into a string
        request_body = request.body.decode('utf-8')
        # change the string into a dictionary. Access via first_name=body["first_name"]
        body = json.loads(request_body)
        print(json.loads(request.body))
        person = forms.PersonForm(json.loads(request.body))
        print(person)
        # if this comes back true, then we can access its clean_data attribute
        if person.is_valid():
            print("all entries are correct. Will save to database")
            print(person.cleaned_data["birth_date"])
            person_to_save = models.Person(first_name=person.cleaned_data["first_name"], last_name=person.cleaned_data["last_name"], email=person.cleaned_data["email"], birth_date=person.cleaned_data["birth_date"], country=person.cleaned_data["country"])
            print("The following person has passed validation and will be saved to the database")
            print(person_to_save)
            return JsonResponse({"email": person_to_save.email, "birth_date": person_to_save.birth_date}, status=status.Code.HTTP_201_CREATED)
            # person_to_save.save()
        else:
            print("Validation process failed")
            print(person.errors)
            #print(form.errors)
        #new_person.save()
        return JsonResponse({"results": person.errors}, status=status.Code.HTTP_201_CREATED)

class PersonDetail(View):
    
    """
    Retreieve, update, or delete a person instance
    """

    def get_object(self, pk):
        try:
            # .get doesn't return the proper JSON response. .get() returns a model.Person object. .filter returns a QuerySet
             return models.Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404("Person not found")
            print("Person not found with that primary key")
        finally:
            print("Done with get_object method")

    def get(self, request, pk):
        print("getting single record with id of {}".format(pk))
        person = self.get_object(pk)
        #dict_person = model_to_dict(person)
        #person_to_send = json.dumps(dict_person)
        print(type(person))
        person_to_send = serializers.serialize('python', [person], ensure_ascii=False)
        # need the 'safe' parameter to allow non-dict objects to be serialized
        return JsonResponse(data=person_to_send, status=status.Code.HTTP_200_OK, safe=False)

# how does django know post vs put?
    def put(self, request, pk):
        person = self.get_object(pk)
        # create person object with new values. If valid, save to database. Otherwise, return an error

    def delete(self, request, pk):
        print("deleting user with id of {}".format(pk))
        return HttpResponse("Deleted")