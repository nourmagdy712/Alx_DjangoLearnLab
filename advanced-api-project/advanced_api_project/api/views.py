from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
import django_filters

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