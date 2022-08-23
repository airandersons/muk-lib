from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . models import Book, BookedBook
from django.urls import reverse
import time
from django.utils import timezone
from datetime import date, datetime, timedelta

def home(request):
    context = {}
    return render(request, "authentication/index.html", context)

def booklister(request):
    info = []
    if request.method == 'POST':
        data = request.POST.items()
        info = list(data)
        print(info)
        logged_student_id = info[1][1]
    return HttpResponseRedirect(reverse('APPLICATION1:borrow', args=(logged_student_id,)))


def borrow(request, logged_student_id):
    new_books = Book.objects.order_by('title')[:]
    student_id = logged_student_id
    context = {'new_books': new_books, 'student_id': student_id}
    return render(request, "authentication/borrow.html", context)

def borrowed(request):
    student_id = request.session['student_id']
    context = {'student_id': student_id}
    return render(request, "authentication/borrowed.html", context)

def checkout(request):
    student_id = request.session['student_id']
    context = {'student_id': student_id}
    return render(request, "authentication/checkout.html", context)

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Please try another Username")
            return redirect('APPLICATION1:home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('APPLICATION1:home')
        
        if len(username)>10:
            messages.error(request, "Username must have only 10 characters")
        
        if pass1 != pass2:
            messages.error(request, "Passwords don't match!")

        if not username.isalnum():
            messages.error(request, "Username should be Alpha-Numeric!")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        return redirect('APPLICATION1:signin')



    return render(request, "authentication/signup.html")

def signin(request):
    request.session['student_id'] = ""
    if request.method =='POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        logged_student_id = None

        user = authenticate(username=username, password=pass1)

        if user is not None:
            if user.is_staff:
                return HttpResponseRedirect(reverse('libralian:library')) 
            else:
                login(request, user)
                fname = user.first_name
                logged_student = User.objects.get(username=username)
                logged_student_id = logged_student.id
                request.session['student_id'] = logged_student_id
                return HttpResponseRedirect(reverse('APPLICATION1:loginview', args=(logged_student_id,))) 
                
        else:
            messages.error(request, "Invalid Credentials!")
            return redirect('APPLICATION1:home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('APPLICATION1:home')

def About(request):
    student_id = request.session['student_id']
    context = {'student_id': student_id}
    return render(request, "authentication/about.html", context)

def loginview(request, logged_student_id):
    context = {'student_id': logged_student_id}
    return render(request, "authentication/loginview.html", context)

def bookrequest(request):
    info = []
    already_booked = ""
    borrow_once = ""
    today = date.today()
    return_date = datetime.today() + timedelta(days=4)
    if request.method == 'POST':
        data = request.POST.items()
        info = list(data)
        book_id = info[1][1]
        request.session['book_id'] = book_id
        student_id = info[2][1]
        book = Book.objects.get(id=book_id)
        student = User.objects.get(id=student_id)
        try:
            booker = BookedBook.objects.get(student_id=student_id)
            borrow_once = "You already have a pending bookrequest and only a single book can be requested at a time."
        except BookedBook.DoesNotExist:
            try:
                booked_checker = BookedBook.objects.get(book_id=book_id)
                already_booked = "Book already Booked, Please choose another copy or wait until it's returned"
            except BookedBook.DoesNotExist:
                current = timezone.now() 
                book.status = "Booked"
                book.save()
                booked = BookedBook.objects.create(book_id=book_id,title=book.title,author=book.author,category=book.category,  bookcover=book.bookcover,user_name=student.username,student_id=student_id,booking_start=current)
                booked.save()
        context = {'book':book, 'student_id': student_id, 'already_booked':already_booked, 'borrow_once':borrow_once, 'today': today, 'return_date': return_date}
    return render(request, 'authentication/checkout.html', context)

def libsearch(request):
    info = []
    empty_search = "Sorry, Book Not Found!"
    student_id = request.session['student_id']
    if request.method == 'POST':
        data = request.POST.items()
        info = list(data)
        search_text = info[1][1]
        search_title = Book.objects.filter(title__icontains=search_text)
        search_author = Book.objects.filter(author__icontains=search_text)
        search_status = Book.objects.filter(status__icontains=search_text)
        search_category = Book.objects.filter(category__icontains=search_text)

        if search_title:
            search_results = search_title
        elif search_author:
            search_results = search_author
        elif search_status:
            search_results = search_status
        elif search_category:
            search_results = search_category 
        else:
            search_results = empty_search
    return render(request, 'authentication/searchresults.html', {'search_results':search_results, 'empty_search': 
    empty_search, 'student_id': student_id})

class Student:
    login = signin