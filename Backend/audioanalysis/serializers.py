from .models import Audio
from rest_framework import serializers

class AudioFileSerializer(serializers.Serializer):
    # Define the fields that get serialized/deserialized
    audio_file = serializers.FileField(required=False)
    s3_url = serializers.URLField(max_length=500, allow_blank=False, required=False)


    def create(self, validated_data):
        """
        Create and return a new 'Audio' instance, given the validated data
        """
        print("IN CREATE METHOD IN AUDIO SERIALIZER")
        print(validated_data)
        return Audio.objects.create(**validated_data)
    
    def validate_audio_file(self, value):
        print("Validating audio file")
        return value

    def validate_s3_url(self, value):
        print("Validating s3 url")
        return value