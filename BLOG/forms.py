from django import forms
from .models import comment_self_anime



class CommentForm(forms.ModelForm):
     
    Comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Name'}))
    class Meta:
        model = comment_self_anime
        fields = ['Comment']
