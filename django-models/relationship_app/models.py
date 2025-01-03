from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    description = models.TextField(default='No description')  # Set default to string

    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        ]

    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} - {self.role}'

    # Define choices for the role field
ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
] 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')
    
     
    
       