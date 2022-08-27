from unicodedata import name
from rest_framework import serializers, status
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password
#from django.contrib.auth.models import User
from .models import *





# class MainRegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'pic']
    
    def validate(self,attrs):
        email=User.objects.filter(username=attrs.get('username')).exists()

        if email:
            raise ValidationError(detail="User with email exists",code=status.HTTP_403_FORBIDDEN)

        username=User.objects.filter(username=attrs.get('username')).exists()

        if username:
            raise ValidationError(detail="User with username exists",code=status.HTTP_403_FORBIDDEN)

        return super().validate(attrs)
        
    # def create(self, validated_data):
    #     user = Profile.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], validated_data['file'])
    #     return user
    
    def create(self,validated_data):
        new_user=User(**validated_data)

        new_user.password=make_password(validated_data.get('password'))

        new_user.save()

        return new_user


        
class FriendSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Friend
        fields = ['user']
    
        
        

class ChatMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'