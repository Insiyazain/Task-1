from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('book/<int:book_id>/',views.book_detail),
    path('members/',views.member_list),
    path('Loan/',views.loan_list),
    path('add-book/', views.add_book)
]

