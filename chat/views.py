from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core import models
from .models import Massages
from django.contrib.auth.models import User
# Create your views here.
@login_required
def chatbox(request,userid):

    massages= Massages.objects.filter(sender=request.user,receiver=userid).order_by('sendtime') |Massages.objects.filter(sender=userid,receiver=request.user).order_by('sendtime')
    username=User.objects.get(pk=userid).username
    context={
        'massages':massages,
        'username':username
    }

    if request.mehtod=='POST':
        newmassage=request.POST['']

        new_massage=Massages(sender=userid,receiver=request.user,massage=newmassage)
        new_massage.save()

    return render(request, 'chat/chatbox.html',context)

@login_required
def chatlist(request):
    friends=models.Friend.objects.filter(receiver=request.user,is_friend=True)
    context={

        'friends':friends
    }

    return render(request, 'chat/chatlist.html',context)
