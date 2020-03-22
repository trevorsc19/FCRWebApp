from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework.response import Response
from django.views import View
from audioanalysis import models
from audioanalysis import forms
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view, authentication_classes, parser_classes
from audioanalysis import speech
from VRWare.authentication.TokenAuthentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework import permissions
import wave

class SuperUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return false



def test_speech(request):
    print("Testing speech")
    p="OSR_us_000_0016_8k" # Audio File title
    speech.run_overview(p)
    return HttpResponse()

@api_view(['POST'])
#@authentication_classes([TokenAuthentication])
@authentication_classes([])
def audio_upload_test(request):
    print(request.data)
    print(request.data.get("audio_file"))
    form = forms.AudioForm(request.POST, request.FILES)
    if form.is_valid():
        print("Audio is valid")
    else:
        print("Audio is not valid")
    return Response({'message': 'Uploaded successful'})
    


# Create your views here.
# postman: body > form-data key: 'audio_file' (has to match name in form class) value: the file
@require_http_methods(["POST"])
def upload_audio(request):
    print("IN AUDIO ANALYSIS APP")
    print("Uploading audio...")

    if request.method == 'POST':
        form = forms.AudioForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            audio_model = models.Audio(audio=cleaned_data['audio_file'])
            audio_model.save()
            return HttpResponse("Audio successfully uploaded");
        else:
            print("Audio is not valid")
            return HttpResponse("Audio Not uploaded");