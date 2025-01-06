from django.shortcuts import render,get_object_or_404,redirect
from .models import Book,Loan,Member
from .forms import Bookform,Memberform,Loanform
from django.contrib import messages #for displaying success messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

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
    if request.method=='POST':
        form=Bookform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Book added successfully!")
            return redirect('home')

        else:
           messages.error(request,"Failed to add book. Please check the form.")

    else:       
      form=Bookform()                         
    
    return render(request, 'home/add_book.html', {'form': form})


def search_books(request):
    query=request.GET.get('q')
    if query:
      books=Book.objects.filter(title__icontains=query)
    else:
      books=Book.objects.all()
    return render(request,'home/search_book.html', {'books':books})

def book_list(request):
   books=Book.objects.all()
   paginator=Paginator(books,5)
   page_number=request.GET.get('page')
   page_obj=paginator.get_page(page_number)
   return render(request,'home/book_list.html',{'page_obj':page_obj})


def filter_book(request):
   books=Book.objects.all()
   sort=request.GET.get('sorts')
   if sort=='publish_date':
      books=books.order_by('-publish_date')
   elif sort=='copies':
      books=books.filter(available_copies__gte=1)
   elif sort=='same_author':
      books=books.filter(author__iexact="Muhammad Zain")   
   return render(request,'home/filter_book.html',{'books':books})      


def my_view(request):
   return render(request,'my_template.html')