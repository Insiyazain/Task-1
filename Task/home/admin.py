from django.contrib import admin
from .models import Loan,Book,Member

# Register your models here.

admin.site.register(Loan)
admin.site.register(Book)
admin.site.register(Member)

