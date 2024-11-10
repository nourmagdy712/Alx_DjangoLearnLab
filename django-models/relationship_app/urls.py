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
    path('register/', views.user_register, name='register'),
    
    # A protected home page (optional)
    path('', views.home, name='home'),
]