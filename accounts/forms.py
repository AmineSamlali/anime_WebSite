from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreatigUseraccount(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Password','type':'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirm Your Password','type':'password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']






