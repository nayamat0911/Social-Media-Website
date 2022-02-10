from distutils.command.upload import upload
from re import T
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    full_name=models.CharField(max_length=263,blank=True)
    dob=models.DateField(blank=True, null=True)
    Bio=models.TextField(max_length=100,blank=True)
    website=models.URLField(blank=True)
    feacbook=models.URLField(blank=True)
    description=models.TextField(max_length=500,blank=True)
    

class Follow(models.Model):
    follower=models.ForeignKey(User, on_delete=models.CASCADE,related_name='follower')
    following=models.ForeignKey(User,on_delete=models.CASCADE, related_name='following')
    created_date=models.DateTimeField(auto_now_add=True)