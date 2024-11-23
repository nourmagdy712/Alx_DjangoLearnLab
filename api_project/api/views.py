from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Query to retrieve all books
    serializer_class = BookSerializer  # Use the BookSerializer for the output

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Fetch all Book objects
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data