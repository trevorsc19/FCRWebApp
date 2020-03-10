from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views import View
from profile import models
import json 
#from profile import status
from django.http import Http404
from django.db import connection
from django.core import serializers
from profile import forms
from django.views.decorators.http import require_http_methods
import logging
from profile.serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

logger = logging.getLogger(__name__)

# docs.djangoproject.com/en/2.2/ref/class-based-views/
# list of HTTP method names this view will accept ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
# "REST framework provides an APIView class, which subclasses Django's View class"
# "Using the APIView class is pretty much the same as using a regular View class, as usual, the incoming request is dispatched to an appropriate handler method"
class ProfileList(APIView):
    """
    List all profiles, or create a new one
    """
    def get(self, request, format=None):
        profiles = models.Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Resposne(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetail(APIView):
    """
    Retrieve, update, or delete a profile instance
    """

    def get_object(self, primary_key):
        try: 
            return models.Profile.objects.get(pk=primary_key)
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        print("Updating")
        profile = self.get_object(pk)
        # Partial = True allows a Patch. django-rest-framework.org/api-guide/serializers/#partial-updates
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def handle_404_method(request, exception):
    from django.template import loader

    print("hi")
    template = loader.get_template('404.html')
    
    context = {
        'key': 'value'
    }
    
    return HttpResponse(template.render(context, request))

def test_404_handler(request):
    # to test handle_404_method
    raise Http404
    #return HttpResponse("<h1>test</h1>", status=404)

@require_http_methods(["POST"])
def upload_document(request):
    if request.method == 'POST':
        print("uploading document")
        newDoc = models.Document(docfile=request.FILES['docfile'])
        newdoc.save()
# postman: body > form-data. key: 'file' value: the file (type is file, not text)
@require_http_methods(["POST"])
def upload_image(request):
    print(request.FILES)
    if request.method == 'POST':
        print("uploading image")
        form = forms.ImageForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            print("image is valid")
            cd = form.cleaned_data
            image_model = models.Image(picture=cd['file'])
            image_model.save()
        else:
            print("image is not valid")
        #form.save()
        return HttpResponse("image succesfully uploaded")
        #return HttpResponse(status=status.Code.HTTP_100_CONTINUE)

