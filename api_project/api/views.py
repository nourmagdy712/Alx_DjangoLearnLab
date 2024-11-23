from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrAdmin

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Query to retrieve all books
    serializer_class = BookSerializer  # Use the BookSerializer for the output
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]  # Apply custom permission

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Assuming each book has an owner

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Fetch all Book objects
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Apply permissions
    permission_classes = [IsAuthenticated]  # Only authenticated users can access
    
    # You can use this to restrict certain actions to admins
    def perform_create(self, serializer):
        if self.request.user.is_staff:  # Allow only admin users to create books
            serializer.save()
        else:
            raise PermissionError("You are not authorized to perform this action.")
        
permission_classes = [IsAdminUser]  # This ensures only admin users can create, update, or delete
