from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from profile import serializers # give VRWare its own serializers.py file and put UserSerializer there
# from serializers import UserSerializer


# https://stackoverflow.com/questions/16857450/how-to-register-users-in-django-rest-framework
class UserList(APIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(APIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
