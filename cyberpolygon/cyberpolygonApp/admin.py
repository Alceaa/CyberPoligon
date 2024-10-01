from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

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

admin.site.register(User, CustomUserAdmin)
