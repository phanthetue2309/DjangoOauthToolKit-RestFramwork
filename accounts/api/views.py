import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializer import CreateUserSerializer, UserSerializer
from ..models import *
from api_base.views.token import TokenView

# Client ID and AccessToken get from Application create in db
from ..ultis import convert_string_array_to_list, convert_list_string_to_space

CLIENT_ID = 'BwRi7vofWyieSaGILcQPfm9ytq6AUrlmjIIt1Sbu'
CLIENT_SECRET = 'FRgi0uEZKj79EfBifp2xk1KSbUqnmVEij88WW3jQXgmTXNOiMlEyuts5YNqzYHHKWG79EqpZjF8erXNCtWaJAxdnGRbOu1FiLXXjueXbHg3t8mvbxvxBYlbsxOlSOdHl'


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """
    Registers user to the server. Input should be in the format:
    {"email": "email", "password": "1234abcd"}
    """
    # Put the data from the request into the serializer
    serializer = CreateUserSerializer(data=request.data)
    # Validate the data
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save()  # save success now we have to generate a key
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    Gets tokens with email and password. Input should be in the format:
    {"email": "email", "password": "1234abcd"}
    """
    scope = ""
    user = None
    try:
        user = User.objects.get(email=request.data['email'])
        role = Role.objects.get(name=user.role)
        scopes = role.scopes
        scopes = convert_string_array_to_list(scopes)
        scope = convert_list_string_to_space(scopes)
    except Exception as e:
        return e

    token_view = TokenView
    r = requests.post(
        'http://127.0.0.1:8000/o/token/',
        data={
            'grant_type': 'password',
            'username': request.data['email'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'scope': 'album:list album:create'
        },
    )
    # return Response(r.json())

    content = r.json()

    data = {
        'id': str(user.id),
        'email': user.email,
        'access_token': content.get('access_token'),
        'refresh_token': content.get('refresh_token'),
        'timestamp': user.timestamp,
    }
    return JsonResponse(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    """
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    """
    r = requests.post(
        'http://127.0.0.1:8000/o/token/',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    """
    Method to revoke tokens.
    {"token": "<token>"}
    """
    r = requests.post(
        'http://127.0.0.1:8000/o/revoke_token/',
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return success message (would be empty otherwise)
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)
