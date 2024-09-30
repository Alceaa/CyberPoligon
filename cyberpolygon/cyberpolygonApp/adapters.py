from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from .verification import send_verification_code_to_telegram

User = get_user_model()

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        if sociallogin.account.provider == 'telegram':
            user = sociallogin.user
            user.telegram_id=sociallogin.account.uid
            user.verification_code=get_random_string(length=6, allowed_chars='0123456789')
            user.save()
            #send_verification_code_to_telegram(user.telegram_id, user.verification_code)