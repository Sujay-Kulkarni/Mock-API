from rest_framework import serializers

from ValidateAccess import settings
from user.models import User


class SafehavenRegistrationSerializer(serializers.ModelSerializer):
    signup_code = serializers.CharField(max_length=200)
    class Meta:
        model = User
        fields = ['signup_code']


