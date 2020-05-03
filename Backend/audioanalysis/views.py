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
import os

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
    # file_name = request.user.username + "_" + pitch_topic + "_" + number
    # file_name = request.data['file_name']
    # need to keep the .wav, or else when we download it from s3, it will be a text file
    file_name = request.FILES["audio_file"].name
    serializer = serializers.AudioFileSerializer(data={"file_name":file_name, "s3_url":"https://vrwarebucket.s3.amazonaws.com/"+file_name})
    if serializer.is_valid():
        print("Audio is valid")
        serializer.save()
        try:
            #with io.BytesIO(request.FILES) as f:
            response = s3_client.upload_fileobj(request.FILES["audio_file"], 'vrwarebucket', file_name)
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

# Create your views here.
# postman: body > form-data key: 'audio_file' (has to match name in form class) value: the file
#@require_http_methods(["POST"])
@api_view(['POST'])
@authentication_classes([])
def upload_audio(request):
    if request.method == 'POST':
        data = {'name':request.FILES['audio_file'].name, 'audio_file':request.data.get('audio_file')}
        file_serializer = serializers.AudioFileSerializer(data=data)
        
        if file_serializer.is_valid():
            file = file_serializer.save()
            p=file.name.split('.', 1)[0] # remove .wav
            speech.run_overview(p)
            # clean_up_temp_directory()
            return HttpResponse("Audio successfully uploaded");
        else:
            print("Audio is not valid")
            print(file_serializer.errors)
            return HttpResponse("Audio Not uploaded");

def clean_up_temp_directory():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    temp_dir = root_dir + "/media/audio"
    print(temp_dir)
    #temp_dir
    
    for filename in os.listdir(temp_dir):
        if filename.endswith(".TextGrid"):
            print("Deleting file " + os.path.join(temp_dir, filename))
            os.remove(os.path.join(temp_dir, filename))
    
    for filename in os.listdir(temp_dir):
        if filename.endswith(".wav"):
            print("Deleting file " + os.path.join(temp_dir, filename))
            os.remove(os.path.join(temp_dir, filename))
            