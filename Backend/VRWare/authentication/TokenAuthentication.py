from rest_framework import status
from django.http import HttpResponse
from rest_framework.authentication import get_authorization_header, BaseAuthentication
# from django.contrib.auth.models import User
from users.models import CustomUser
import jwt, json

# thinkster.io/tutorials/django-json-api/authentication (for creating custom user too)
# medium article jyoti gautam 

class TokenAuthentication(BaseAuthentication):
    model = None

    def get_model(self):
        return CustomUser
    
    def authenticate(self, request):
        print('authenticate method')
        print("authenticating user " + request.data['username'])
        auth = get_authorization_header(request).split()
        print("Authorization header")
        for a in auth:
            print(a)
       
        #if not auth or auth[1].lower() != b'token':
         #   print("None")
          #  return None
        
        if not auth:
            print("No authorization header")
            return None

        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header'
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1]
            if token=='null':
                msg = 'null tokens not allowed'
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg='Invalid token header. Token string should not contain invalid characters'
            raise exceptions.AuthenticationFailed(msg)
                
        return self.authenticate_credentials(token)
        
    def authenticate_credentials(self, token):
        print("Authenticate credentials...")
        model = self.get_model()
        # Expiration time is automatically verified and raises ExpiredSignatureError if the expiration time is in the past
        try:
            payload = jwt.decode(token, 'SECRET', algorithms=['HS256']) 
        except jwt.ExpiredSignatureError:
            print("Token expired. Please use refresh token to get a new one")
            # check for 403 in front end, send refresh token to get new access token
            return HttpResponse({'Error': "Token is invalid"}, status=403)
        print("PAYLOAD")
        print(payload)
        email = payload['email']
        userid = payload['id']
        #msg = {'Error': 'Token mismatch', 'status':'401'}

        try:
            user = CustomUser.objects.get(email=email, id=userid)
        
        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            return HttpResponse({'Error': 'Internal server error'}, status='500')
        
        return (user, token)