from django import forms
from .models import Chat
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['username', 'post', 'image']