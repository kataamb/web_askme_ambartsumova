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




class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) # to change widget
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    avatar = forms.ImageField(allow_empty_file=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password' ]

    def save(self, commit=True):

        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

    def clean(self):
        super().clean()

        pswd = self.cleaned_data['password']
        check_pswd = self.cleaned_data['confirm_password']

        if pswd != check_pswd:
            raise ValidationError("Passwords do not match")




class EditForm(forms.ModelForm):
    avatar = forms.ImageField(allow_empty_file=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name' ]

    def save(self, commit=True):

        user = super().save(commit=False)

        user.save()
        return user

    def clean(self):
        super().clean()