from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from user.serializers import SafehavenRegistrationSerializer
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
            if code=="ABCDEFG":
                return Response({"status": status.HTTP_200_OK,"message":"Success", "data":{"user_details": {"firstname": "Divya","lastname": "Mansinghani", "gender": {"key": "F", "value": "Female"},"dob": "10-15-1997"}}}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "failed","message":"data not found"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response('ok')








