from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils.crypto import get_random_string
from django.core.mail import send_mail


@api_view(['POST'])
def register(request):
    data = request.data
    user = SignUPSerializer(data = data)

    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user = User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'], 
                email = data['email'] , 
                username = data['email'] , 
                password = make_password(data['password']),
            )
            return Response(
                {'details':'Your account registered susccessfully!' },
                    status=status.HTTP_201_CREATED
                    )
        else:
            return Response(
                {'error':'This email already exists!' },
                    status=status.HTTP_400_BAD_REQUEST
                    )
    else:
        return Response(user.errors)
            
            
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = UserSerializer(request.user, many=False)
    return Response(user.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user
    data = request.data

    user.first_name = data['first_name']
    user.username = data['email']
    user.last_name = data['last_name']
    user.email = data['email']

    user.save()
    serializer = UserSerializer(user,many=False)
    return Response(
        { 'updated':serializer.data},
         status=status.HTTP_200_OK
     )



def get_current_host(request):
    """
    Returns the host for this site (useful to build absolute URLs in templates)
    """
    protocol = request.is_secure() and 'https' or 'https'
    host = request.get_host()
    return "{protocol}://{host}/".format(protocol=protocol, host=host)


@api_view(['POST'])
def forget_password(request):
      data = request.data
      user = get_object_or_404(User, email=data['email'])
      token = get_random_string(40)
      expire_date = datetime.now() + timedelta(minutes=60)
      user.profile.reset_password_token = token
      user.profile.reset_password_expire = expire_date
      user.profile.save()
      host = get_current_host(request)
      link = "http://localhost:8000/api/reset_password/{token}".format(token=token)
      body = "We've received a request to reset the password for your account. To help you regain access to your account, please follow the instructions below to reset your password: {link}".format(link=link)
      send_mail(
          "Password reset from E-Market",
          body,
          "E-Market@gmail.com",
          [data['email']]
      )
      return Response(
          {
              'status' : True,
              'message':'Check your {email} mail'.format(email=data['email']),
              'E-Market' : 'Thanks...'
          },
             status=status.HTTP_200_OK
       )



@api_view(['POST'])
def reset_password(request, token):
      data = request.data
      user = get_object_or_404(User, profile__reset_password_token=token)
      if user.profile.reset_password_expire.replace(tzinfo=None) < datetime.now():
          return Response({'error':'Token is Expired'}, status=status.HTTP_401_UNAUTHORIZED)
      if data['password'] != data['confirmPassword']:
          return Response({'error': 'Passwords do not match'}, status=status.HTTP_401_UNAUTHORIZ)
      
      user.password = make_password(data['password'])
      user.profile.reset_password_token = ""
      user.profile.reset_password_expire = None
      user.profile.save()
      user.save()
      return Response(
          {
            'status' : True,
            'message':'Your password has been changed',
            'E-Market' : 'Thanks...'
        },
         status=status.HTTP_200_OK
         )