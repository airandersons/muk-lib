from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from APPLICATION1.models import Book, BookedBook
from . models import TakenBook,ReturnedBook
from datetime import date, datetime, timedelta

def library(request):
    days_remaining = []
    books = Book.objects.order_by('title')[:]
    number = books.count()
    booked_books = BookedBook.objects.order_by('title')[:]
    taken_books = TakenBook.objects.order_by('date_taken')[:]
    num2 = taken_books.count()
    returned_books = ReturnedBook.objects.order_by('date_taken')[:]
    num = booked_books.count()
    context = {'num2': num2, 'number': number, 'num': num, 'booked_books': booked_books, 'taken_books':taken_books, 'returned_books':returned_books}
    return render(request, 'libralian/index.html', context)

def approve(request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        student_id = request.POST.get('student_id')
        book = Book.objects.get(id=book_id)
        book.status = "Unavailable"
        book.save()
        del_book = BookedBook.objects.get(book_id=book_id)
        del_book.delete()
        taken = TakenBook.objects.create(book_id=book_id,book_title=book.title,username=del_book.user_name,category=book.category,  student_id=student_id,date_taken=del_book.booking_start, return_date=datetime.today()+timedelta(days=4))
        taken.save()
    return HttpResponseRedirect(reverse('libralian:library'))

def bookreturn(request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        student_id = request.POST.get('student_id')
        book = Book.objects.get(id=book_id)
        book.status = "Available"
        book.save()
        del_book = TakenBook.objects.get(book_id=book_id)
        del_book.delete()
        fine = 0
        if date.today() >= del_book.return_date+timedelta(days=3):
            fine = 5000
        elif date.today() >= del_book.return_date+timedelta(days=10):
            fine = 10000
        else:
            fine = 0
        return_book = ReturnedBook.objects.create(book_id=book_id,book_title=book.title,username=del_book.username,category=book.category,  student_id=student_id,date_taken=del_book.date_taken, return_date=del_book.return_date, actual_return_date=datetime.today(), fine=fine)
        return_book.save()
    return HttpResponseRedirect(reverse('libralian:library'))

def fine(request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        student_id = request.POST.get('student_id')
        book = ReturnedBook.objects.get(book_id=book_id)
        book.fine = 0
        book.save()
    return HttpResponseRedirect(reverse('libralian:library'))
    
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('APPLICATION1:home')

def newbook(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        status = request.POST.get('status')
        category = request.POST.get('category')
        description = request.POST.get('description')
        cover = request.POST.get('cover')
        newbook = Book.objects.create(title=title, author=author, status=status, category=category, description=description, bookcover=cover)
        newbook.save()
    return HttpResponseRedirect(reverse('libralian:library'))