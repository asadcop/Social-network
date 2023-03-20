from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   path('box/', views.chatbox),
   path('list/', views.chatlist)
]
