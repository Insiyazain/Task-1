from django.shortcuts import render,get_object_or_404,redirect
from .models import Book,Loan,Member
from .forms import Bookform,Memberform,Loanform
from django.contrib import messages #for displaying success messages

# Create your views here.

def index(request):
    books=Book.objects.all()
    return render(request,"home/index.html", {'books': books})

def book_detail(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'home/book_detail.html', {'book': book})

def member_list(request):
    members=Member.objects.all()
    return render(request,'home/member_list.html',{'members': members})

def loan_list(request):
    loans=Loan.objects.all()
    return render(request,'home/loan_list.html',{'loans':loans})

def add_book(request):
    if request.method=='post':
        form=Bookform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Book added successfully!")
            return redirect('home')

    else:
        form=Bookform()                         
    
    return render(request, 'home/add_book.html', {'form': form})