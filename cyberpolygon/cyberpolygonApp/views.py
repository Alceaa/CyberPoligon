from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.yandex.views import YandexAuth2Adapter
from allauth.socialaccount.providers.telegram.views import LoginView
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.views import ObtainAuthToken
from django.views.decorators.csrf import csrf_exempt
from dj_rest_auth.registration.views import SocialLoginView
from django_otp.plugins.otp_totp.models import TOTPDevice
from .verification import send_verification_code_to_telegram
import qrcode
import io
import base64

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CommentsListCreate(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class CommentsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class UserAvatarListCreate(generics.ListCreateAPIView):
    queryset = UserAvatar.objects.all()
    serializer_class = UserAvatarSerializer

class UserAvatarRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAvatar.objects.all()
    serializer_class = UserAvatarSerializer

class YandexLogin(SocialLoginView):
    adapter_class = YandexAuth2Adapter

class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    
class TelegramLogin(SocialLoginView):
    adapter_class = LoginView
    
class RegisterView(APIView):
    @csrf_exempt
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(ObtainAuthToken):
    @csrf_exempt
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data['username']
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user_qs = User.objects.filter(username=username)
        if user_qs.count() == 0:
            return Response({"detail": "Пользователя не существует"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(request, username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({"detail": "Успешная авторизация"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Неправильный пароль"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
       @csrf_exempt
       def post(self, request):
        logout(request)
        return Response({"detail": "Выход успешно выполнен"}, status=status.HTTP_200_OK)

class GenerateQRcode(APIView): 
    @csrf_exempt 
    def post(self, request):
        if request.method == 'POST':
            if request.data.get('username'):
                try:
                    user = User.objects.get(username=request.data.get('username'))
                except User.DoesNotExist:
                    return Response({'detail': 'Пользователя с таким именем не существует'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'detail': 'Имя пользователя не указано'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                device = TOTPDevice.objects.get(user=user)
            except Exception:
                device = TOTPDevice.objects.create(user=user)
        
            uri = device.config_url
            img = qrcode.make(uri)
            buffered = io.BytesIO()
            img.save(buffered)
            img_str = base64.b64encode(buffered.getvalue()).decode()
            return Response({
                'qr_code': f"data:image/png;base64,{img_str}",
            })
        return Response({'detail': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class VerifyOtp(APIView):   
    @csrf_exempt 
    def post(self, request):
        if request.method == 'POST':
            otp = request.data.get('otp')
            try:
                user = User.objects.get(username=request.data.get('username'))
            except User.DoesNotExist:
                return Response({'detail': 'Пользователя с таким именем не существует'}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                device = TOTPDevice.objects.get(user=user)
                if device.verify_token(otp):
                    return Response({'detail': "Успешно"}, status=status.HTTP_200_OK)
                else:
                    return Response({'detail': 'Неправильный код'}, status=status.HTTP_400_BAD_REQUEST)
            except TOTPDevice.DoesNotExist:
                return Response({'detail': 'Для этого пользователя не установлено OTP'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'detail': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
class VerifyTelegram(APIView):
    @csrf_exempt 
    def post(self, request):
        if request.method == 'POST':
            telegramId = request.data.get('telegram_id')
            try:
                user = User.objects.get(telegram_id=telegramId)
                verificationCode = user.verification_code
                send_verification_code_to_telegram(telegramId, verificationCode)
                return Response({'detail': "Успешно"}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'detail': 'Пользователя с таким телеграмом не существует'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
       
def init(request):
    return render(
            request,
            'empty.html'
        )

def home(request):
    return render(
            request,
            'home.html'
    )
