from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"), 
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('activate/<uid>/<token>', views.activate, name="activate"),
    path('forgot-password',views.forgot_password,name="forgot-password"),
    path('forgot-password/<uid>/<token>', views.forgot_password_active_url,name='forgot-password-url'),
    path('resat-password', views.resat_password,name='resat-password'),


    
]
