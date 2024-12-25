from django.shortcuts import render,get_object_or_404
from .models import Book,Loan,Member

# Create your views here.

def index(request):
    books=Book.objects.all()
    return render(request,"home/index.html", {'books': books})

def book_detail(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'home/book_detail.html', {'book': book})

