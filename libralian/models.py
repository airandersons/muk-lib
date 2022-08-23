from django.db import models
from django.utils import timezone
from datetime import date, datetime, timedelta

class TakenBook(models.Model):
    book_id = models.IntegerField()
    book_title = models.TextField(max_length=20)
    username = models.TextField(max_length=20)
    category = models.TextField(max_length=20)
    student_id = models.IntegerField()
    date_taken = models.DateField(default=datetime.today())
    return_date = models.DateField(default=datetime.today())

class ReturnedBook(models.Model):
    book_id = models.IntegerField()
    book_title = models.TextField(max_length=20)
    username = models.TextField(max_length=20)
    category = models.TextField(max_length=20)
    student_id = models.IntegerField()
    date_taken = models.DateField(default=datetime.today())
    return_date = models.DateField(default=datetime.today())
    actual_return_date = models.DateField(default=datetime.today())
    fine = models.IntegerField()