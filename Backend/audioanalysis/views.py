from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views import View
from audioanalysis import models
from audioanalysis import forms
from django.views.decorators.http import require_http_methods
#import myspsolution as mysp

def test_speech():
    print("Testing spech")
    

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