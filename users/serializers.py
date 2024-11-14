from rest_framework import serializers
from .models import CustomUser
from djoser.serializers import UserSerializer as DjoserUserSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        ref_name = 'CustomUserSerializer'  

class CustomDjoserUserSerializer(DjoserUserSerializer):
    class Meta(DjoserUserSerializer.Meta):
        ref_name = 'DjoserUserSerializer'