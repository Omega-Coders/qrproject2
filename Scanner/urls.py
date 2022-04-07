#from django import views
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
  path('',views.home, name='home'),
  path('signin',views.signin,name="signin"),
  path('signup',views.signup,name="signup"),
  #path('',views.signout,name="signout"),
   path('activate/<uidb64>/<token>', views.activate, name='activate'),
   path('scanner',views.scanner,name="scanner"),
    path('index', views.index, name='index'),
    path('video_stream', views.video_stream, name='video_stream'),


    path('link/<date>', views.link, name='link'),



]