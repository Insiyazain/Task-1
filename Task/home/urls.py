from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('book/<int:book_id>/',views.book_detail),
    path('members/',views.member_list),
    path('Loan/',views.loan_list),
    path('add-book/', views.add_book),
    path('search/', views.search_books, name='search_books'),
    path('book_list/',views.book_list)
]

