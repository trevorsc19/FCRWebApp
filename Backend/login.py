from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.contrib.auth.models import User
from users.models import CustomUser
import jwt, json
import datetime
import time
import pytz
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from django.views.decorators.csrf import ensure_csrf_cookie
from users.serializers import UserSerializer
from profile.models import Profile
from profile.serializers import ProfileSerializer

@api_view(['POST'])
# @ensure_csrf_cookie
def login_view(request):
    print("Loggin in...")
    username = request.data['username']
    password = request.data['password']
    print(request.user.is_authenticated)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print("Login successful")
        return Response({"message":"Login successful"})
    else:
        print("Not authenticated")


@api_view(['POST'])
def logout_view(request):
    print("Logging out user ")
    print(request.user)
    logout(request)
    return Response({'msg': 'Logout successful'})

@api_view(['POST'])
def register_user(request):
    print("Creating a new user")
    print(request.data)
    data = {'username':request.data["userName"], 'password':request.data["password"], 'email':request.data["email"]}
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        print("Valid")
        user = serializer.save()
        # have to create profile data and link it to user
        data = {'user':user, 'first_name':None, 'last_name':None, 'email':request.data["email"], 'birth_date':None, 'country':None}
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            print("Profile data is valid")
            serializer.save()
        else:
            print("Profile data is not valid")
            print(serializer.errors)
        #profile = Profile(user=user, first_name=None, last_name=None, email=request.data["email"], birth_date=None, country=None)

        return Response({'user': serializer.data})
    print("data not valid")
    print(serializer.errors)
     # user = User.objects.create_user(username, email_from_profile_object, password)

@api_view(['POST'])
def verify_session(request):
    print("Verifying session")
    print(request.user)
    if request.user.is_authenticated:
        print("Verifying session for user with id of " + str(request.user.id))
        return Response({"msg":"session verified"},status=status.HTTP_200_OK)
    else:
        print("User is not authenticated")
        return Response(status=status.HTTP_401_UNAUTHORIZED)