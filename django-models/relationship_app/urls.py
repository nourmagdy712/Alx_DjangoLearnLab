from django.urls import path
from .views import list_books
from .views import LibraryDetailView 

urlpatterns = [
    path('library/', LibraryDetailView.as_view(), name='library-detail'),
    path('list_books/', list_books, name='list_books'),
]