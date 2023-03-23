from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from core import models
from .models import Messages
from django.contrib.auth.models import User
# Create your views here.
@login_required
def chatbox(request,senderr):
    
    senduser=User.objects.get(pk=senderr)
    if request.method=='POST':
        
        newmessage=request.POST['message']
        new_message=Messages(sender=request.user,receiver=senduser,message=newmessage)
        new_message.save()
    
    messages= Messages.objects.filter(sender=senderr,receiver=request.user).order_by('sendtime')|Messages.objects.filter(sender=request.user,receiver=senderr).order_by('sendtime')
    
    
    context={
        'messages':messages,
        'senduser':senduser,
    }
    print(messages)
    

    return render(request, 'chat/chatbox.html',context)


@login_required
def chatlist(request):
    friends=models.Friend.objects.filter(receiver=request.user,is_friend=True)|models.Friend.objects.filter(sender=request.user,is_friend=True)
    print(friends)
    context={

        'friends':friends
    }

    return render(request, 'chat/chatlist.html',context)
