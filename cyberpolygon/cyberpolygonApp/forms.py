from django import forms
from .models import *
from .models import Images

class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image']
