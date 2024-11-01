# Create Operation
from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Retrieve Operation

retrieved_book = Book.objects.all()
print(retrieved_book)

# Update Operation

book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

# Delete Operation

book.delete()
deleted_books = Book.objects.all()
print(deleted_books)