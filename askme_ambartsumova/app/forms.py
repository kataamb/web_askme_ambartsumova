from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import CharField

from app.models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)




    def clean(self):
        super().clean()

        user = User.objects.get(username = self.cleaned_data['username'])

        print(user, user.password)

