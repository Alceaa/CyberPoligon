from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.init, name='init'),
    path('home/', views.home, name='home'),
    path("accounts/", include("allauth.urls")),
]
