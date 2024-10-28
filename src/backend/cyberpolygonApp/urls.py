from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.init, name='init'),
    path('home/', views.home, name='home'),
    path("accounts/", include("allauth_2fa.urls")),
    path("accounts/", include("allauth.urls")),
    path('martor/', include('martor.urls')),
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

    #markdown
    path('api/get_markdown_post/', views.GetMarkdownPost.as_view(), name='get_markdown_post'),
    path('api/markdown_uploader/', views.markdown_uploader, name='markdown_uploader_page'),

    #tests
    path('api/tests/', views.TestGetPost.as_view(), name="get_post_test"),
    path('api/tests/content/', views.TestQuestionsAnswersPost.as_view(), name="test_questions_answers_post" ),
    path('api/tests/check/', views.TestCheckAnswers.as_view(), name="test_check_answers"),

    #vagrant
    path('api/vagrant/start', views.VagrantStartTask.as_view(), name="vagrant_start_task"),
    path('api/vagrant/stop', views.VagrantStopTask.as_view(), name="vagrant_stop_task"),
    path('api/vagrant/relaod', views.VagrantReloadTask.as_view(), name="vagrant_reload_task"),

    #Tasks
    path('api/tasks/check_flag', views.TaskCheckFlag.as_view(), name="task_check_flag"),
]
