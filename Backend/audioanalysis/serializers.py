from .models import Audio
from rest_framework import serializers

class AudioSerializer(serializers.Serializer):
    # Define the fields that get serialized/deserialized
    s3_url = serializers.URLField(max_length=500, allow_blank=False)

    def create(self, validated_data):
        """
        Create and return a new 'Audio' instance, given the validated data
        """
        print("IN CREATE METHOD IN AUDIO SERIALIZER")
        print(validated_data)
        return Audio.objects.create(**validated_data)