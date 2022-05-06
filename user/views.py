from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from user.serializers import SafehavenRegistrationSerializer,SafehavenSignupSerializer
from user.models import User


class ValidateAccessCode(APIView):
    permission_classes =()
    authentication_classes = ()

    serializer_class=SafehavenRegistrationSerializer
    def post(self,request):
        try:

            serializer = SafehavenRegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            payload = serializer.validated_data
            
            code = payload.pop('signup_code')
            if code is not None:
                try:
                    if code=="ABCDEFG":
                        return Response({"status": status.HTTP_200_OK,"message":"Success", "data":{"user_details": {"firstname": "Divya","lastname": "Mansinghani", "gender": {"key": "F", "value": "Female"},"dob": "10-15-1997"}}}, status=status.HTTP_200_OK)
                    else:
                        return Response({"status": "failed","message":"Invalid Signup Code"}, status=status.HTTP_404_NOT_FOUND)
                except:
                    return Response('Not found')
        except:
            return Response('The Field cannot be empty',status=status.HTTP_400_BAD_REQUEST)

class Signup(APIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class=SafehavenSignupSerializer
    def post(self, request):
        serializer = SafehavenSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payload = serializer.validated_data
        email=payload.pop('email')
        password=payload.pop('password')
        try:
            if email=='Snehal.Limburkar@newscapeconsulting.com' and password=='Sneha@1997':
                return Response({"status":status.HTTP_201_CREATED,"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI0ODQ0MTQ5LCJqdGkiOiJjYzAzMWM0MTYyMzU0OGZiYWVkYmVjNzMzMmFmOTlkZCIsInVzZXJfaWQiOjksInBlcm1pc3Npb25zIjoibGltaXRlZCJ9.KxC9By5SwYlXBO-ysjBNuzTRuDxZmeTB-kE3SfSlDB4",
                                   "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNzQzMjU0OSwianRpIjoiMmFhODFkYjUzMzQ1NDc2OGFhMjljZTQ1YTcwMjgwMDMiLCJ1c2VyX2lkIjo5LCJwZXJtaXNzaW9ucyI6ImxpbWl0ZWQifQ.RBwJKoB2o3M7wZfL3_z0srJTGOeeinaPD_NW91tx8B8"},status=status.HTTP_201_CREATED)
            else:
                return Response('Invalid Credentials')
        except:
            return Response('ok')






