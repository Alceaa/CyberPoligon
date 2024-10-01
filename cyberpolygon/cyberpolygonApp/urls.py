from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.init, name='init'),
    path('home/', views.home, name='home'),
    path("accounts/", include("allauth_2fa.urls")),
    path("accounts/", include("allauth.urls")),
    path('api/user', views.UserListCreate.as_view()),
    
    re_path(r'^api/user/(?P<pk>[0-9]+)/$', views.UserRetrieveUpdateDestroy.as_view() ),

    path('api/categories/', views.CategoryListCreate.as_view()),
    re_path(r'^api/categories/(?P<pk>[0-9]+)/$', views.CategoryRetrieveUpdateDestroy.as_view() ),

    path('api/tasks/', views.TaskListCreate.as_view()),
    re_path(r'^api/tasks/(?P<pk>[0-9]+)/$', views.TaskRetrieveUpdateDestroy.as_view() ),

    path('api/comments/', views.CommentsListCreate.as_view()),
    re_path(r'^api/comments/(?P<pk>[0-9]+)/$', views.CommentsRetrieveUpdateDestroy.as_view() ),

    path('api/avatars/', views.UserAvatarListCreate.as_view()),
    re_path(r'^api/avatars/(?P<pk>[0-9]+)/$', views.UserAvatarRetrieveUpdateDestroy.as_view() ),

    #api auth
    path('api/auth/yandex/', views.YandexLogin.as_view(), name='yandex_login_api'),
    path('api/auth/github/', views.GitHubLogin.as_view(), name='github_login_api'),
    path('api/auth/telegram/', views.TelegramLogin.as_view(), name='telegram_login_api'),
    path('api/auth/signup/', views.RegisterView.as_view(), name='registration'),
    path('api/auth/login/', views.LoginView.as_view(), name='login'),
    path('api/auth/logout/', views.LogoutView.as_view(), name='logout'),

    #otp
    path('api/generate_qr/', views.GenerateQRcode.as_view(), name='generate_qr_code'),
    path('api/verify_otp/', views.VerifyOtp.as_view(), name='verify_otp'),
    path('api/verify_telegram/', views.VerifyTelegram.as_view(), name='verify_telegram'),
]
