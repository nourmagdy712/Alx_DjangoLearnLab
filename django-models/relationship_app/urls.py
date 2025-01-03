from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('library/', LibraryDetailView.as_view(), name='library-detail'),
    path('list_books/', list_books, name='list_books'),
     # Login and Logout views using Django's built-in class-based views
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # Custom Register view
    path('register/', views.register, name='register'),
    
    # A protected home page (optional)
    path('', views.home, name='home'),

    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    path('add/', views.add_book, name='add_book/'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book/'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book/'),
]