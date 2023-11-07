from rest_framework import serializers
from django.contrib.auth.models import User


class SignUPSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password',)
        extra_kwargs = {
            "first_name":{"required":True, "allow_blank":False},
            "last_name":{"required":True, "allow_blank":False},
            "email":{"required":True, "allow_blank":False},
            "password":{"write_only": True, "required":True, "allow_blank":False, "min_length":8}
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            "password":{"write_only": True}
        }