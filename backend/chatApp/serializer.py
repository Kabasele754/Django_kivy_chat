from unicodedata import name
from rest_framework import serializers
from .function import attempt_json_deserialize
from django.contrib.auth.models import User
from .models import *


# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Profile.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'profile']
class RegisterSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='profile.city', required=False)
    country = serializers.CharField(source='profile.country', required=False)
    profile_pic = serializers.ImageField(source='profile.profile_pic', required=False)
    is_online = serializers.BooleanField(source='profile.is_online', required=False)
    is_active = serializers.BooleanField(source='profile.is_active', required=False)
    class Meta:
        model = User
        #removed url from fields
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'city', 'country', 'profile_pic', 'is_online', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True},
        }
        def create(self,validated_data):
            user = User.objects.create_user(
                                            username=validated_data['username'],
                                            first_name=validated_data['first_name'],
                                            last_name=validated_data['last_name'],
                                            email=validated_data['email'])
            user.set_password(validated_data['password'])
            user.save()
            #added fields from profile
            user.profile.city = validated_data['city']
            user.profile.country = validated_data['country']
            user.profile.bio = validated_data['bio']
            return user

class MainRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfilSerializer(serializers.ModelSerializer):
    #user = MainRegisterSerializer()
    
    class Meta:
        model = User
        fields = ('id','username','phone_number','email', 'date_of_birth', 'password','friends') 
        
        
class FriendSerializer(serializers.ModelSerializer):
    user = ProfilSerializer()
    class Meta:
        model = Friend
        fields = '__all__'
        
    def create(self, validated_data):
        type_data = validated_data.pop('user')
        friend = Friend.objects.create(**validated_data)
        for t_data in type_data:
            User.objects.create(friend=friend, **t_data)
        return friend
        
    # def create(self, validated_data):
    #     request = self.context['request']
        
    #     user_data = request.data.get('user')
    #     user_data = attempt_json_deserialize(user_data, expect_type=dict)
    #     user = User.objects.create(**user_data)
    #     validated_data['user'] = user
        
    #     instance = super().create(validated_data)

    #     return instance
        
        
class ChatMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'