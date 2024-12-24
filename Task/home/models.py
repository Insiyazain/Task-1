from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    isbn=models.CharField(max_length=100)
    publish_date=models.DateField(auto_now_add=True)
    available_copies=models.IntegerField()

    def __str__(self):
        return self.title


class Member(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    join_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Loan(models.Model):
    book=models.ForeignKey('Book',on_delete=models.CASCADE)
    member=models.ForeignKey('Member',on_delete=models.CASCADE)
    loan_date=models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
      return f"{self.book.title} loaned to {self.member.name}"
    



