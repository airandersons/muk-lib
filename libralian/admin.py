from django.contrib import admin
from . models import TakenBook, ReturnedBook

admin.site.register(TakenBook)
admin.site.register(ReturnedBook)
