from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

# Content-Type has to be set to application/json in postman
@api_view(['POST'])
def login_view(request):
    print("adsf")
    username = request.data['username']
    password = request.data['password']
    print("Username: {} password: {}".format(username, password))
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        print("User is authenticated")
        print(user.email)
        login(request, user)
        return JsonResponse({
            'username': request.user.username, 
            'email': request.user.email
        })
    else:
        print("User is NOT authenticated")
# https://stackoverflow.com/questions/12615154/how-to-get-the-currently-logged-in-users-user-id-in-django