from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation to ensure the publication_year is not in the future
    def validate_publication_year(self, value):
        from datetime import date
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to represent books associated with the author
    books = BookSerializer(many=True, read_only=True)

class Meta:
    model = Author
    fields = ['name', 'books']
