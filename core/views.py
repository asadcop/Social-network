from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models

# Create your views here.
def home(request):
    
    return render(request,"core/home.html")

@login_required
def timeline(request):
    posts=models.Post.objects.all().order_by("-id")
    likes=models.Like.objects.all()
    context={
        'posts':posts,
        'likes':likes,
    }
    if request.method=='POST':
        postid=request.POST['like']
        post_get=models.Post.objects.get(pk=postid)
        is_liked=models.Like.objects.get(liker=request.user,post=postid)
        if is_liked is not None:
            is_liked.delete()
            post_get.numbers_of_likes=post_get.numbers_of_likes-1
        else:
            new_like=models.Like(postid,request.user)

            title=str(request.user.username)+" was like you post"

            new_notification=models.Notification(title=title,resiver=post_get.user)
            new_notification.save()
            new_like.save()
            post_get.numbers_of_likes=post_get.numbers_of_likes+1
        post_get.save()
    return render(request, "core/timeline.html",context)


@login_required
def notification(request):
    notification_get=models.Notification.objects.filter(resiver=request.user)
    context={
        'notifications':notification_get,
    }

    return render(request, "core/notification.html", context)

@login_required
def friend(request):
    
    friend_request=models.Friend.objects.filter(receiver=request.user)
    context={
        'friend_request':friend_request,
    }
    if request.method=='POST':
        sender=request.POST['']
        accapt=request.POST['']
        accapt_friend=models.Friend.objects.get(sender=sender,receiver=request.user)
        if accapt:
            accapt_friend.is_friend=True
            accapt_friend.save()
        else:
            accapt_friend.delete()    



    return render(request,"core/friend.html",context)

@login_required
def addfriend(request):
    if request.method == 'POST':
        addfriend_name=request.POST['']
        get_new_friend_object=User.objects.get(username=addfriend_name)
        addnew_friend=models.Friend(sender=get_new_friend_object,receiver=request.user)
        addnew_friend.save()
        title=str(request.user.username)+" was send a friend request"

        new_notification=models.Notification(title=title,resiver=get_new_friend_object)
        new_notification.save()
        
    return redirect('/friends')

@login_required
def profile(request):
    
    return render(request,"core/profile.html")
