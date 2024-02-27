from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "hx-post": "/registration/check-username/",
        "hx-trigger": "keyup delay:1s",
        "hx-target": "#username-error",
        "autocomplete": "off"
    }))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control", 'autocomplete': 'off'}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = (
            "username", "password1", "password2", "email",
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control not-dark","placeholder": "Login"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control not-dark", "placeholder": "Password"}))

    class Meta:
        model = User
        fields = (
            "username", "password"
        )
