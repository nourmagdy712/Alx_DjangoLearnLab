from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView 

urlpatterns = [
    path('library/', LibraryDetailView.as_view(), name='library-detail'),
    path('list_books/', list_books, name='list_books'),
     path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('', views.home, name='home'),  # Optional home page
]