from allauth.account.forms import SignupForm
from django import forms
from .models import *

class CustomSignupForm(SignupForm):
    def signup(self, request, user):
        userRole = Role.objects.create(role_name = "user")
        user.id_role = userRole
        user.save()
        return user