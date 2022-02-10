from django.urls import reverse
from cmath import log
from re import search
from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth.decorators import login_required

from app_login.models import UserProfile,Follow
from django.contrib.auth.models import User
from app_post.models import Like,Post
# Create your views here.
@login_required
def Home(request):
    following_list = Follow.objects.filter(follower=request.user)
    liked_post=Like.objects.filter(user=request.user)
    liked_post_list=liked_post.values_list('post', flat=True)
    
    if request.method == "GET":
        search = request.GET.get('search_item', ' ')
        result = User.objects.filter(username__icontains=search)


    home_context={
        'title':'Home',
        'content':"this home",
        'searching_all':search,
        'result_item':result,
        'following_listed':following_list,
        'liked_post_list':liked_post_list,
    }
    return render(request,'app_post/home.html',context=home_context) 


@login_required
def liked(request, pk):
    post=Post.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post, user=request.user)
    if not already_liked:
        liked_post=Like(post=post,user=request.user)
        liked_post.save()
    return HttpResponseRedirect(reverse('Home'))

@login_required
def Unliked(request, pk):
    post=Post.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post, user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('Home'))