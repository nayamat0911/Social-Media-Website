from atexit import register
from xml.dom.domreg import registered
import django
from django.shortcuts import render
from .forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect

from .models import UserProfile,Follow
from .forms import Edit_profile
# Create your views here.

# Signup section =====================================

def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == "POST":
        form=CreateNewUser(data=request.POST)
        if form.is_valid():
            user=form.save()
            registered=True
            user_profile=UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('app_login:login_page'))

    sign_up_form={
        "title":"sign Up",
        "sign_form":form,
    }

    return render(request, 'app_login/sign_up.html', context=sign_up_form)



# Login section =====================================

def login_page(request):
    log_form=AuthenticationForm()
    if request.method=="POST":
        log_form=AuthenticationForm(data=request.POST)
        if log_form.is_valid():
            username=log_form.cleaned_data.get('username')
            password=log_form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('Home'))
    login_context={
        "title":"login",
        "log_in":log_form
    }
    return render(request, 'app_login/login.html',context=login_context)




# edit Porfile section =====================================

@login_required
def edit_profile(request):
    current_user=UserProfile.objects.get(user=request.user)
    form=Edit_profile(instance=current_user)
    if request.method == "POST":
        form = Edit_profile(request.POST, request.FILES , instance = current_user)
        if form.is_valid():
            form.save(commit=True)
            form=Edit_profile(instance = current_user)
            return HttpResponseRedirect(reverse('app_login:User_Profile'))
    edit={
        'title':"Profile",
        "edti_form_":form
    }
    return render(request, "app_login/profile.html",context=edit)




# Logout section =====================================

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_login:login_page'))


 # Profile + Post section =====================================
from app_post.forms import PostForm

@login_required
def User_Profile(request):
    form=PostForm()
    if request.method == "POST":
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('Home'))
    photo_context={
        'title':"Profile",
        "post_form":form
    }
    return render(request, 'app_login/User_Profile.html',context=photo_context)




from django.contrib.auth.models import User
@login_required
def User__view(request, username):
    user_pro = User.objects.get(username=username)
    already_followed=Follow.objects.filter(follower = request.user, following = user_pro)
    if user_pro == request.user:
        return HttpResponseRedirect(reverse('app_login:User_Profile'))
    otheruser = {
        'title':"other-profile",
        'others_user_profile':user_pro,
        'already_followed':already_followed
    }

    return render(request, 'app_login/other_user.html', context=otheruser)
 

@login_required
def follow(request, username):
    following_user=User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    if not already_followed:
        followed_user=Follow(follower=follower_user, following=following_user)
        followed_user.save()
        pass
        return HttpResponseRedirect(reverse('app_login:User__view',kwargs={'username':username}))

@login_required
def unfollow(request, username):
    following_user=User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('app_login:User__view',kwargs={'username':username}))





    
