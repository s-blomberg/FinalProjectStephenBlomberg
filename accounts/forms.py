from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address is already in use.")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # Define custom layout
        self.helper.layout = Layout(
            Field('username', css_class='form-control-lg', placeholder='Enter your username'),
            Field('email', css_class='form-control-lg', placeholder='Enter your email'),
            Field('password1', css_class='form-control-lg'),
            Field('password2', css_class='form-control-lg'),
        )

        # Add a submit button
        self.helper.add_input(Submit('submit', 'Sign Up'))
