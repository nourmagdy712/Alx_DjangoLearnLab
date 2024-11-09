from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()  # Using the related_name 'books' defined in the ForeignKey
    for book in books:
        print(book.title)

# Query 2: List all books in a specific library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Using the related_name 'libraries' defined in the ManyToManyField
    for book in books:
        print(book.title)

# Query 3: Retrieve the librarian for a specific library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # Using the related_name 'librarian' defined in OneToOneField
    print(f"Librarian for {library_name}: {librarian.name}")

if __name__ == "__main__":
    # Example Queries
    print("Books by Author 'J.K. Rowling':")
    books_by_author("J.K. Rowling")
    
    print("\nBooks in 'Central Library':")
    books_in_library("Central Library")
    
    print("\nLibrarian for 'Central Library':")
    librarian_for_library("Central Library")