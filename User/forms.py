from django import forms
from .models import emp,user_normal
class empForm(forms.ModelForm):
    class Meta:
        model=emp
        fields="__all__"

class userREF(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    password=forms.CharField(max_length=20)
    confirm_password=forms.CharField(max_length=20)

