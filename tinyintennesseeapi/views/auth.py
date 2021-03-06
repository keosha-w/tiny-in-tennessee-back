from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from tinyintennesseeapi.models import TitUser

from django.contrib.auth import authenticate


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a gamer

    Method arguments:
      request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    authenticated_user = authenticate(username=username, password=password)

    # If authentication was successful, respond with their token
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key,
            'is_staff': authenticated_user.is_staff,
            'user_id': authenticated_user.id
        } # sending this data to the front end so that we can set it on local storage. 
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)
    
    
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new user for authentication
    '''

    new_user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        is_staff=request.data['is_staff']
    )
    
    tit_user = TitUser.objects.create(
        user=new_user
    )

    token = Token.objects.create(user=tit_user.user)
    data = {'token': token.key,
            'is_staff': new_user.is_staff,
            'user_id': new_user.id}
    return Response(data)
