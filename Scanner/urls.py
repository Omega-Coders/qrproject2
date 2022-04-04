#from django import views
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
  path('',views.home, name='home'),
  path('signin',views.signin,name="signin"),
  path('signup',views.signup,name="signup"),
  path('',views.signout,name="signout"),  
]