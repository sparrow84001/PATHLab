from django import forms
from .models import emp
class empForm(forms.ModelForm):
    class Meta:
        model=emp
        fields="__all__"