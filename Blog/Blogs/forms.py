from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Comment

class signUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


class createPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description']

        
class commentPost(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']