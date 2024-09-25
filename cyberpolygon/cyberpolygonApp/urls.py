from django.urls import path, include, re_path
from . import views
from allauth.account.views import ConfirmEmailView, LoginView, LogoutView
from dj_rest_auth.registration.views import ConfirmEmailView

urlpatterns = [
    path('', views.init, name='init'),
    path('home/', views.home, name='home'),
    path("accounts/", include("allauth_2fa.urls")),
    path("accounts/", include("allauth.urls")),
    path('accounts/confirm-email//', ConfirmEmailView.as_view(), name='account_confirm_email'),
    path('api/user', views.UserListCreate.as_view()),
    
    re_path(r'^api/user/(?P<pk>[0-9]+)/$', views.UserRetrieveUpdateDestroy.as_view() ),

    path('api/roles/', views.RoleListCreate.as_view()),
    re_path(r'^api/roles/(?P<pk>[0-9]+)/$', views.RoleRetrieveUpdateDestroy.as_view() ),

    path('api/categories/', views.CategoryListCreate.as_view()),
    re_path(r'^api/categories/(?P<pk>[0-9]+)/$', views.CategoryRetrieveUpdateDestroy.as_view() ),

    path('api/tasks/', views.TaskListCreate.as_view()),
    re_path(r'^api/tasks/(?P<pk>[0-9]+)/$', views.TaskRetrieveUpdateDestroy.as_view() ),

    path('api/comments/', views.CommentsListCreate.as_view()),
    re_path(r'^api/comments/(?P<pk>[0-9]+)/$', views.CommentsRetrieveUpdateDestroy.as_view() ),

    path('api/avatars/', views.UserAvatarListCreate.as_view()),
    re_path(r'^api/avatars/(?P<pk>[0-9]+)/$', views.UserAvatarRetrieveUpdateDestroy.as_view() ),

    #api auth
    path('api/auth/social/', views.SocialLogin.as_view(), name='social_login'),
    path('api/auth/signup/', views.RegisterView.as_view(), name='registration'),
    path('api/auth/login/', views.LoginView.as_view(), name='login'),
    path('api/auth/logout/', views.LogoutView.as_view(), name='logout'),
]
