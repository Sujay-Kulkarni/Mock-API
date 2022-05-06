from rest_framework import serializers

from ValidateAccess import settings
from user.models import User, Signup


class SafehavenRegistrationSerializer(serializers.ModelSerializer):
    signup_code = serializers.CharField(max_length=200)
    class Meta:
        model = User
        fields = ['signup_code']

class SafehavenSignupSerializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=200)
    password=serializers.CharField(max_length=200)
    class Meta:
        model= Signup
        fields=['email','password']


