from rest_framework import serializers
from .models import *
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('__all__')

class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAvatar
        fields = ('__all__')


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, write_only=True)
    username = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def validate_email(self, email):
        if User.objects.filter(email=email):
            raise serializers.ValidationError(
                "A user is already registered with this e-mail address.")
        return email

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise serializers.ValidationError(
                "A user is already registered with this username.")
        return username

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        return user
    
class LoginSerializer(serializers.Serializer):
       email = serializers.EmailField()
       username = serializers.CharField()
       password = serializers.CharField(write_only=True)

class SocialLoginSerializer(serializers.Serializer):
    provider = serializers.CharField()
    access_token = serializers.CharField()

    def validate(self, data):
        provider = data.get('provider')
        if provider not in ['google', 'github']:
            raise serializers.ValidationError("Unsupported provider.")
        return data