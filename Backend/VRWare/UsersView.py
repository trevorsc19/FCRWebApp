"""
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

# https://stackoverflow.com/questions/16857450/how-to-register-users-in-django-rest-framework
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
"""