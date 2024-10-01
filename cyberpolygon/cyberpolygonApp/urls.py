from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.init, name='init'),
    path('creat_post/', views.creat_post, name = 'creat_post'),
    path('post_list/', views.creat_post, name = 'post_list'),
    path('upload/', views.upload_image, name='upload_image'),
]