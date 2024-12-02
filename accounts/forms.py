from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email Address")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Customize the fields
        labels = {
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
