from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# Create your views here.

"""
from django.http import HttpResponse
def index(request): return HttpResponse("Welcome to my book store.”)

#In urls.py:

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("books/", include("book_store.urls")),
    path("admin/", admin.site.urls),
]
"""

# View to list books - restricted by permission
@permission_required('book_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# View to create a new book - restricted by permission
@permission_required('book_app.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Assume we process form data here
        book = Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            published_date=request.POST['published_date']
        )
        return redirect('book_list')
    return render(request, 'create_book.html')

# View to edit a book - restricted by permission
@permission_required('book_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.save()
        return redirect('book_list')
    return render(request, 'edit_book.html', {'book': book})

# View to delete a book - restricted by permission
@permission_required('book_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

def search_books(request):
    query = request.GET.get('query')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})