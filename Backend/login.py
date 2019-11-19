from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.contrib.auth.models import User
import jwt, json
import datetime

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
  
    if user:
        
        payload = {
            'id': user.id,
            'email': user.email
        }

        jwt_token = {'token': jwt.encode(payload, "SECRET", headers={'exp':1574120220})}
        print("Sending following token to user:")
        print(jwt.decode(jwt_token['token'], 'SECRET', algorithms=['HS256']))
    
        return Response(jwt_token, status=200, content_type="application/json")
    else:
        return Response(json.dumps({"Error": "Invalid credentails"}), status=400, content_type="application/json")
