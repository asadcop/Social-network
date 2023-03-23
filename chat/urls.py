from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   path('box/<senderr>', views.chatbox,name='chatbox'),
   path('send/<sender>', views.sendmessage,name='sendmessage'),
   path('list/', views.chatlist,name='chatlist'),
]
