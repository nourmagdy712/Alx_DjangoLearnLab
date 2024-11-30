from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
import django_filters

# List View: Retrieve all books
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []  # No authentication required for listing books

# Detail View: Retrieve a single book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []  # No authentication required for viewing book details

# Create View: Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books

    def perform_create(self, serializer):
        # Custom logic for book creation (e.g., logging, setting default values)
        # Call the parent class's perform_create to save the object
        serializer.save(created_by=self.request.user)

# Update View: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books

    def perform_update(self, serializer):
        # Custom logic for book update
        serializer.save(updated_by=self.request.user)

# Delete View: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete books

class BookFilter(django_filters.FilterSet):
    # Filter by title
    title = django_filters.CharFilter(lookup_expr='icontains')
    # Filter by author's name
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    # Filter by publication year
    publication_year = django_filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']  # Enable search on title and author's name
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering by title



