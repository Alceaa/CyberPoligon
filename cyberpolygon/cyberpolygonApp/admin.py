from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.db import models
from martor.widgets import AdminMartorWidget


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  
        (                      
            'verification',
            {
                'fields': (
                    'telegram_id', 'verification_code'
                ),
            },
        ),
    )
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

@admin.register(Test, Question, Answer, CorrectAnswer)
class TestsAdmin(admin.ModelAdmin):
    pass

@admin.register(Task, UserDoingTask)
class TasksAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, CustomUserAdmin)
admin.site.register(Post, PostAdmin)