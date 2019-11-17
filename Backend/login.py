from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse

# Content-Type has to be set to application/json in postman
@api_view(['POST'])
def login_view(request):
    username = request.data['username']
    password = request.data['password']
    print("Username: {} password: {}".format(username, password))
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        print("User is authenticated")
        login(request, user)
        print("after login")
        print(user.username)
        
        return JsonResponse({
            'username': reqeuest.user.username
        })
    
    else:
        print("User is NOT authenticated")