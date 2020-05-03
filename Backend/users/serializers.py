from .models import CustomUser
from rest_framework import serializers

"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'id']
"""

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True, 
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email')
    
    def create(self, validated_data):
        print("creating....")
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_password(self, value):
        return value