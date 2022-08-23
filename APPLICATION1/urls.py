from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'APPLICATION1'
urlpatterns = [
    path('', views.home, name="home"),
    path('loginview/<int:logged_student_id>/', views.loginview, name="loginview"),
    path('borrow/<int:logged_student_id>/', views.borrow, name="borrow"),
     path('borrowed/', views.borrowed, name="borrowed"),
    path('checkout/', views.checkout, name="checkout"),
    path('signup', views.signup, name="signup"),
    path('signin', views.Student.login, name="signin"),
    path('signout', views.signout, name="signout"),
    path('about', views.About, name="About"),
    path('bookrequest/', views.bookrequest, name='bookrequest'),
    path('booklister', views.booklister, name='booklister'),
    path('libsearch/', views.libsearch, name='libsearch'),
]