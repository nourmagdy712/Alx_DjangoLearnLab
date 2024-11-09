from django.contrib import admin

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display these fields in the list view
    list_filter = ('author', 'publication_year')  # Add filters for these fields
    search_fields = ('title', 'author')  # Add search capabilities for these fields

# Register your models here.
from .models import Book
admin.site.register(Book, BookAdmin)
