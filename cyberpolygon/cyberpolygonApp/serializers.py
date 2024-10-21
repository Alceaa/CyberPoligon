from rest_framework import serializers
from .models import *
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'telegram_id', 'user_data')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'created_at')

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'task_id', 'user_id', 'comment', 'rating', 'created_at')

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
                "Пользователь с такой почтой уже существует")
        return email

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise serializers.ValidationError(
                "Пользователь с таким именем уже существует")
        return username

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Пароли не совпадают")
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


class TestSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=False)

    class Meta:
        model = Test
        fields = ['title', 'description', 'created_at']

    def validate(self, title):
        if Test.objects.filter(title=title):
            raise serializers.ValidationError(
                "Такой тест уже существует")
        return title
    
    def save(self, data):
        test = Test.objects.create(title=data['title'], description=data['description'], created_at=datetime.date.today())
        return test