from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserInfo

class BasicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')

class UserInfoSerializer(serializers.ModelSerializer):
    user = BasicUserSerializer()
    class Meta:
        model = UserInfo
        fields = '__all__'
