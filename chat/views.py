from django.shortcuts import render

# Create your views here.

def chatbox(request):

    
    return render(request, 'chat/chatbox.html')


def chatlist(request):
    return render(request, 'chat/chatlist.html')
