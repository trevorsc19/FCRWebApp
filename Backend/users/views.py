#from django.contrib.auth.models import User
from users.models import CustomUser
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework import generics
from users.serializers import UserSerializer

# https://stackoverflow.com/questions/16857450/how-to-register-users-in-django-rest-framework
class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []

class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'
    authentication_classes = []

    def get_object(self):
        print("request")
        print(self.kwargs)
        print(self.__dict__)
        print("Searching for user with id of " + str(self.kwargs['user_id']))
        user = User.objects.get(pk=self.kwargs['user_id'])
        print(user)
        return user

class CreateUser(generics.CreateAPIView):
    print("Creating user")
    serializer_class = UserSerializer