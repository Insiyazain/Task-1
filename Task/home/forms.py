from django import forms
from .models import Book,Member,Loan

class Bookform(forms.ModelForm):
    class Meta:
       model=Book
       fields=['title','author','isbn','available_copies']

class Memberform(forms.ModelForm):
    class Meta:
        model=Member
        fields=['name','email','phone']

class Loanform(forms.ModelForm):
    class Meta:
        model=Loan
        fields=['book','member','loan_date','return_date']       

    
