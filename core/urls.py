from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('timeline/', views.timeline, name="timeline"),
    path('notification/', views.notification, name="notification"),
    path('profile/', views.profile, name="profile"),
    path('friends/',views.friend,name='friend'),
    path('add-friends/',views.addfriend,name='add-friend'),
      
]
