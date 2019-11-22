from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.contrib.auth.models import User
import jwt, json
import datetime
import time
import pytz

# Content-Type has to be set to application/json in postman
@api_view(['POST'])
def login_view(request):
    if not request.data:
        return Response({'Error': "Please provide username/password"}, status="400")
    
    username = request.data['username']
    password = request.data['password']
    print("Username: {} password: {}".format(username, password))
    try:
        user = User.objects.get(username=username)
        
        if not user.check_password(password):
            raise User.DoesNotExist

    except User.DoesNotExist: # if user not found or password is wrong
        return Response({'Error': "Invalid username/password"}, status="400")
  
    if request.user.is_authenticated:
        print("user is authenticated")
    else:
        print("User is not authenticated")

    if user:
        
        payload = {
            'id': user.id,
            'email': user.email
        }

        to_exp = datetime.datetime.now() + datetime.timedelta(minutes=1)
        unix_time = time.mktime(to_exp.timetuple())
        jwt_token = {'token': jwt.encode(payload, "SECRET", 'HS256',headers={'exp': unix_time})}
        # UTC to EST local time
        print("Expiration date of token is " + str(to_exp.astimezone(pytz.timezone('US/Eastern'))))
        print("Sending following token to user:")
        print(jwt.decode(jwt_token['token'], 'SECRET', algorithms=['HS256'], options={'verify_exp': True}))
        print("HEADERS")
        print(jwt.get_unverified_header(jwt_token['token'])['exp'])
        return Response(jwt_token, status=200, content_type="application/json")
    
    else:
        return Response(json.dumps({"Error": "Invalid credentails"}), status=400, content_type="application/json")
