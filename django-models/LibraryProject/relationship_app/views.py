from django.shortcuts import render

# Create your views here.
from relationship_app.models import Book
from django.views.generic import DetailView
from relationship_app.models import Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all Book objects from the database
    
    # Render the 'relationship_app/list_books.html' template with the 'books' context
    return render(request, 'relationship_app/list_books.html', {'books': books})