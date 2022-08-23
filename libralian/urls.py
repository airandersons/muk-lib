from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'libralian'
urlpatterns = [
    path('library', views.library, name='library'),
    path('approve', views.approve, name='approve'),
    path('bookreturn', views.bookreturn, name='bookreturn'),
    path('fine', views.fine, name='fine'),
    path('signout', views.signout, name='signout'),
    path('newbook', views.newbook, name='newbook'),
]