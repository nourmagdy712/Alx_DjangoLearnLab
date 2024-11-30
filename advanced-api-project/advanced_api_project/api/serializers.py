from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    # Serializer for Book model
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        # Custom validation to ensure publication year is not in the future
        from datetime import date
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Serializer for Author model
    books = BookSerializer(many=True, read_only=True)
    # Nested BookSerializer to show books associated with the author

    class Meta:
        model = Author
        fields = ['name', 'books']