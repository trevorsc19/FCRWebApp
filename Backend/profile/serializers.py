from rest_framework import serializers
from profile.models import Profile, COUNTRY_CHOICES
from django.contrib.auth.models import User

class ProfileSerializer(serializers.Serializer):
    # Define the fields that get serialzied/deserialzied
    
    id = serializers.IntegerField(read_only=True)
    user = serializers.OneToOneField(User)
    #account_created = serializers.DateTimeField(auto_now_add=True)
    last_modified = serializers.DateTimeField(auto_now=True)
    first_name = models.CharField(null=True, max_length=30)
    last_name = mdoels.CharField(null=True, max_length=30)
    email = models.EmailField(null=False, default=None, max_length=50)
    birth_date = models.DateField(null=True)
    country = models.CharField(null=True, default=None, max_length=100)

    def create(self, vaidated_data)
        """
        Create and return a new 'Profile' instance, given the validated data
        """
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data)

        """
        Update and return an existing 'Profile' instance, given the validated data
        """
        # do i neeed last_modified?
        instance.first_name = validated_data,get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance