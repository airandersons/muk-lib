from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import date, datetime, timedelta

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=13, default="Available")
    category = models.CharField(max_length=20, null=True)
    bookcover=models.ImageField()
    description = models.TextField(null=True, blank=True)

class BookedBook(models.Model):
    book_id = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=20, null=True)
    bookcover=models.ImageField()
    user_name = models.CharField(max_length=50)
    student_id = models.IntegerField()
    booking_start = models.DateTimeField(default=datetime.today())
    booking_end = models.DateTimeField(default=datetime.today()+timedelta(days=4))
     
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class BookRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    req_date = models.DateField('Date of book request', null=True, blank=True)
    #return_date = req_date + datetime.timedelta(days=8) 
    book_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.book_id

class Fines(models.Model):
    book_id = models.IntegerField()
    student_id = models.IntegerField()
    actual_return_date = models.DateField()
    extra_days = models.IntegerField()
    fine = models.IntegerField()