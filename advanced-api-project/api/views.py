from django.shortcuts import render

# Create your views here.
from django_filters import rest_framework
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
import django_filters
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Book, Author

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


class BookApiTests(APITestCase):
    
    def setUp(self):
        """
        Create test data for the Book model and the associated Author model.
        """
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.token = Token.objects.create(user=self.user)
        
        # Create an Author
        self.author = Author.objects.create(name="J.K. Rowling")
        
        # Create a Book
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )
        
        # Define the API URL for the book
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})

    def test_create_book(self):
        """
        Ensure we can create a new book with proper authentication.
        """
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.pk
        }
        response = self.client.post(
            self.book_list_url,
            data,
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Ensure the book count is 2 after creation

    def test_read_book(self):
        """
        Ensure we can retrieve a book's detail.
        """
        response = self.client.get(
            self.book_detail_url,
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)  # Ensure correct book data is returned

    def test_update_book(self):
        """
        Ensure we can update a book's information.
        """
        data = {'title': 'Updated Book Title'}
        response = self.client.patch(
            self.book_detail_url,
            data,
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )
        self.book.refresh_from_db()  # Refresh the object from the database
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.book.title, 'Updated Book Title')  # Ensure the book title has been updated

    def test_delete_book(self):
        """
        Ensure we can delete a book.
        """
        response = self.client.delete(
            self.book_detail_url,
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Ensure the book is deleted

    def test_permissions_for_unauthenticated_user(self):
        """
        Ensure that unauthenticated users cannot create or modify books.
        """
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2024,
            'author': self.author.pk
        }
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Unauthorized request

    def test_filter_books_by_author(self):
        """
        Test filtering books by author.
        """
        Book.objects.create(title="Harry Potter and the Chamber of Secrets", publication_year=1998, author=self.author)
        response = self.client.get(
            self.book_list_url + '?author=' + str(self.author.pk),
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # We should have 2 books by the same author

    def test_search_books_by_title(self):
        """
        Test searching for books by title.
        """
        response = self.client.get(
            self.book_list_url + '?search=Harry',
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)  # We should get at least one book matching the search query

    def test_order_books_by_publication_year(self):
        """
        Test ordering books by publication year.
        """
        Book.objects.create(title="Harry Potter and the Prisoner of Azkaban", publication_year=1999, author=self.author)
        response = self.client.get(
            self.book_list_url + '?ordering=publication_year',
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1997)  # First item should be the earliest publication year (1997)
