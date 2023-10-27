from socket import fromshare
from django import forms
from .models import Post

class AddPostForm(forms.ModelForm) :
    
    class Meta:
        model = Post
        fields = ('image', 'caption')

