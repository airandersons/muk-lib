from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'APPLICATION1'
urlpatterns = [
    path('', views.home, name="home"),
    path('borrow/', views.borrow, name="borrow"),
     path('borrowed/', views.borrowed, name="borrowed"),
    path('checkout/', views.checkout, name="checkout"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('about', views.About, name="About"),
    path('loginview', views.loginview, name="loginview"),
]