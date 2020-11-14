from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name','type':"text",'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name','type':"text",'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your Email','type':"text",'class':'form-control'}))

    class Meta:
        model = User
        fields  = ['first_name','last_name','email']
class ProfileForm(forms.ModelForm):
    PRF_phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your phone','type':"text",'class':'form-control'}))
    PRF_Location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Location','type':"text",'class':'form-control'}))
    PRF_profile_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'text-center center-block file-upload'}))
    class Meta:
        model = Profile
        fields = ['PRF_phone','PRF_Location','PRF_profile_image']
        

class PasswordChangeForm_F(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'old Password ','type':"password",'class':'form-control',}))
    new_password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'New Password ','type':"password",'class':'form-control'}))
    new_password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Replay New Password','type':"password",'class':'form-control'}))

    class Meta:
        model = PasswordChangeForm
        fields = '__all__'