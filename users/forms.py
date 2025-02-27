from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser

class ForgotPasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            return ValidationError('Email does\'nt end with "@gmail.com"')
        user = CustomUser.objects.filter(username = username, email = email)
        if not user.exists():
            return ValidationError('Email does\'nt match with username')
        return cleaned_data