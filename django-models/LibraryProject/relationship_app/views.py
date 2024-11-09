from django.shortcuts import render

# Create your views here.
from relationship_app.models import Book
from django.views.generic import DetailView
from relationship_app.models import Library


# Function-based view to list all books
def list_books(request):
    return render(request, "relationship_app/list_books.html", {"books": Book.objects.all()})