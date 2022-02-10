from dataclasses import field
import email
from pyexpat import model
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CreateNewUser(UserCreationForm):
    email=forms.EmailField(required=True,label="", widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username=forms.CharField(required=True,label="", widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1=forms.CharField(required=True,label="", widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(required=True,label="", widget=forms.PasswordInput(attrs={'placeholder':'Confirmation Password'}))
    class Meta:
        model=User
        fields=('email','username','password1','password2')

class Edit_profile(forms.ModelForm):
    dob=forms.DateField(widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model=UserProfile
        exclude=('user',)