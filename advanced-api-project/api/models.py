from django.db import models

# Create your models here.
class Author(models.Model):
    # Model to represent an author
    name = models.CharField(max_length=255)  # Author's name

class Book(models.Model):
    # Model to represent a book
    title = models.CharField(max_length=255)  # Title of the book
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # Establishes a relationship with the Author model. One author can have multiple books.
