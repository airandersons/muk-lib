from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    borrower_id = models.CharField(max_length=100,null=True,blank=True)
    Uploaded = models.DateTimeField(auto_now=True)
    Due_date = models.DateTimeField(auto_now=True)
    books= models.FileField()
    bookcover=models.ImageField()
    def __str__(self):
        return self.title 
     