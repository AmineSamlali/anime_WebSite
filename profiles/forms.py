from django import forms
from .models import Profile
from django.contrib.auth.models import User

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
        