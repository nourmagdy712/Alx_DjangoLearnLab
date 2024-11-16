# Delete Operation

from bookshelf.models import Book

book.delete()
deleted_books = Book.objects.all()
print(deleted_books)