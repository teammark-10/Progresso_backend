from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer,validationSerializer,otpSerializer
import otp_verification

@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def validation(request):
    serializer = validationSerializer(data=request.data)

    if serializer.is_valid():
        num=serializer.data['number']
        stat=otp_verification.verification.sent_otp(num)
        return Response(stat)
    

@api_view(['POST'])
def otpveri(request):
    serializer = otpSerializer(data=request.data)

    if serializer.is_valid():
        validated_data = serializer.validated_data  # Access validated data
        serializer.save()  # Save the validated data
        print(validated_data)  # Print or process the validated data
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)