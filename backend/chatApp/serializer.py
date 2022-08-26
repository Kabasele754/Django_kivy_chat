from unicodedata import name
from rest_framework import serializers, status
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Profile.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'profile']


class MainRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfilSerializer(serializers.HyperlinkedModelSerializer):
    user = MainRegisterSerializer()
    
    class Meta:
        model = Profile
        fields = ('user' ,'name','pic') 
    
    def validate(self,attrs):
        email=Profile.objects.filter(username=attrs.get('username')).exists()

        if email:
            raise ValidationError(detail="User with email exists",code=status.HTTP_403_FORBIDDEN)

        username=Profile.objects.filter(username=attrs.get('username')).exists()

        if username:
            raise ValidationError(detail="User with username exists",code=status.HTTP_403_FORBIDDEN)

        return super().validate(attrs)
        
    # def create(self, validated_data):
    #     user = Profile.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], validated_data['file'])
    #     return user
    
    def create(self,validated_data):
        new_user=Profile(**validated_data)

        new_user.password=make_password(validated_data.get('password'))

        new_user.save()

        return new_user


        
class FriendSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfilSerializer()
    class Meta:
        model = Friend
        fields = '__all__'
    
        
        

class ChatMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'