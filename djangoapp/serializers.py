from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class validationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['name','email','gender','dob','weight','height']  # Exclude this field