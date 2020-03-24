from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
# from django.contrib.auth.models import User
from users.models import CustomUser
import jwt, json
import datetime
import time
import pytz


@api_view(['POST'])
def login_view(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print("Login successful")
        return Response({"message":"Login successful"})
    else:
        print("Not authenticated")

def session_test(request):
    print("This is a test")
    print(request.user.id)


# Content-Type has to be set to application/json in postman
"""
@api_view(['POST'])
def login_view(request):

    print("LOGIN VIEW")
    
    if not request.data:
        return Response({'Error': "Please provide username/password"}, status="400")
    
    username = request.data['username']
    password = request.data['password']
    print("Username: {} password: {}".format(username, password))
    try:
        print("1")
        user = CustomUser.objects.get(username=username)
        print("2")
        print(user)
        print(user.check_password(password))
        
        if not user.check_password(password):
            print("User was found, but password is incorrect")
            raise User.DoesNotExist

    except CustomUser.DoesNotExist: # if user not found or password is wrong
        # raise User.DoesNotExist
        return Response({'Error': "Invalid username/password"}, status="400")
  
    if request.user.is_authenticated:
        print("user is authenticated")
    else:
        print("User is not authenticated")

    #exp_time = 60
    exp_time = 500
    if user:
        
        payload = { 
            'id': user.id,
            'email': user.email, 
            'exp': time.time() + exp_time
        }
        

        to_exp = datetime.datetime.now() + datetime.timedelta(minutes=1)
        unix_time = time.mktime(to_exp.timetuple())
        #jwt_token = {'token': jwt.encode(payload, "SECRET", 'HS256',headers={'exp': unix_time})}
        jwt_token = {'access_token': jwt.encode(payload, "SECRET", 'HS256'), 
            'refresh_token': jwt.encode({'exp': time.time() + 120}, "SECRET", "HS256")} # refresh token will expire after 15 days (1296000 seconds)
        #jwt_token = jwt.encode({'user_id':123, 'exp': time.time()+60},"SECRET", algorithm='HS256')
        # UTC to EST local time
        print("Expiration date of token is " + str(to_exp.astimezone(pytz.timezone('US/Eastern'))))
        print("Sending following token to user:")
        print(jwt.decode(jwt_token['access_token'], 'SECRET', algorithms=['HS256']))
        return Response(jwt_token, status=200, content_type="application/json")
    
    else:
        print("Returning error to view")
        return Response(json.dumps({"Error": "Invalid credentails"}), status=400, content_type="application/json")

@api_view(['POST'])
def token_test(request):
    print("Testing token....")
"""