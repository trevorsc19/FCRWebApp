from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from profile import serializers # give VRWare its own serializers.py file and put UserSerializer there
# from serializers import UserSerializer
from rest_framework import generics


# https://stackoverflow.com/questions/16857450/how-to-register-users-in-django-rest-framework
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = 'user_id'

    def get_queryset(self):
        print("request")
        print(self.kwargs)
        print("Searching for user with id of " + str(self.kwargs['user_id']))
        user = User.objects.get(pk=self.kwargs['user_id'])
        print(user)
        return user
