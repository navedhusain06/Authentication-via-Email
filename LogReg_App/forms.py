# forms.py
from django import forms
from django.contrib.auth.models import User

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Email address")
