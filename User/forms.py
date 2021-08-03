from django import forms
from .models import user_normal

class userREF(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    password=forms.CharField(max_length=20)
    confirm_password=forms.CharField(max_length=20)

