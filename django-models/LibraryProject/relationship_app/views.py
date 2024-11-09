from django.shortcuts import render

# Create your views here.
from relationship_app.models import Book
from django.views.generic import DetailView
from relationship_app.models import Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', Book.objects.all())

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # Optional: Customize the context if needed (e.g., to add extra data)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Add books in the library to the context
        return context