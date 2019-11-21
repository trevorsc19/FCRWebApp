from rest_framework import status
from django.http import HttpResponse
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from django.contrib.auth.models import User
import jwt, json

class TokenAuthentication(BaseAuthentication):
    print("AUTHENTICATION CLASS")
    model = None

    def get_model(self):
        return User
    
    def authenticate(self, request):
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
        payload = jwt.decode(token, 'SECRET_KEY') 
        print("PAYLOAD")
        print(payload)
        email = payload['email']
        userid = payload['id']
        msg = {'Error': 'Token mismatch', 'status':'401'}

        try:
            user = User.objects.get(email=email, id=userid, is_activte=true)

            if not user.token['token'] == token:
                raise exceptions.AuthenticationFailed(msg)
        
        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            return HttpResponse({'Error': 'Internal server error'}, status='500')
        
        return (user, token)