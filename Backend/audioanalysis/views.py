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
import boto3
from botocore.exceptions import ClientError
import io
from audioanalysis import serializers

class SuperUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return false

@api_view(['GET'])
@authentication_classes([])
def test_s3(request):
    #boto3.set_stream_logger('')
    print("Testing s3...")
    s3 = boto3.resource('s3')

    for bucket in s3.buckets.all():
        print(bucket.name)
        for obj in bucket.objects.all():
            print(obj.key)


    s3 = boto3.resource('s3')
    audio_bucket = s3.Bucket('vrwarebucket')
    for audio_bucket_object in audio_bucket.objects.all():
        print(audio_bucket_object)

@api_view(['POST'])
@authentication_classes([])
def upload_s3_test(request):
    # need to get logged in user so that we can tie the S3 URL to the user
    print("Testing S3 upload...")

    s3_client = boto3.client('s3')
    # https://vrwarebucket.s3.amazonaws.com/s3_upload_file.wav
    #form = forms.AudioForm(request.POST, request.FILES)
    #if form.is_valid():
    serializer = serializers.AudioSerializer(data={"s3_url":"https://vrwarebucket.s3.amazonaws.com/s3_upload_file.wav"})
    if serializer.is_valid():
        print("Audio is valid")
        serializer.save()
        try:
            #with io.BytesIO(request.FILES) as f:
            response = s3_client.upload_fileobj(request.FILES["audio_file"], 'vrwarebucket', 's3_upload_file.wav')
            # add id of audio entry to logged in profile row
            print(request.user)
            # add url to audio analysis table
        except ClientError as e:
            return Response({'message': 'Exception thrown'})
    else:
        print("Audio is not valid")
        print(serializer.errors)
        return Response({'message': 'Audio is not valid'})
    return Response({'message': 'Uploaded successful'})



def test_speech(request):
    print("Testing speech")
    p="OSR_us_000_0016_8k" # Audio File title
    #speech.run_overview(p)
    p="male"
    #speech.run_overview(p)
    p="OSR_us_000_0035_8k"
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