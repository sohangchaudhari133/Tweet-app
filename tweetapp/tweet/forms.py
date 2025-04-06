from django import forms
from .models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','photo']

class UserRegistrationForm(UserCreationForm):
    # use of UserCreationForm is to create a new user 
    email = forms.EmailField()
    class Meta:
        model = User
        # fields are in tuple and when we create own then fields are not in tuple
        # 2 passwords are used for security purpose
        fields = ('username','email','password1','password2')

