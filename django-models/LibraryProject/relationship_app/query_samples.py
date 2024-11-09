from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # Get the Author instance
        books = Book.objects.filter(author=author)     # Get all Books related to this author
        return books
    except Author.DoesNotExist:
        print(f"No author found with the name: {author_name}")
        return []

# Query 2: List all books in a specific library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Get the Library instance
        books = library.books.all()  # Access the related books through the ManyToMany field
        return books
    except Library.DoesNotExist:
        print(f"No library found with the name: {library_name}")
        return []

# Query 3: Retrieve the librarian for a library using Librarian.objects.get(library=...)
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Get the Library instance
        librarian = Librarian.objects.get(library=library)  # Get the associated Librarian
        return librarian
    except Library.DoesNotExist:
        print(f"No library found with the name: {library_name}")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to the library: {library_name}")
        return None

if __name__ == "__main__":
    # Sample queries to test the relationships
    print("Books by Author 'J.K. Rowling':")
    for book in books_by_author("J.K. Rowling"):
        print(f"- {book.title}")

    print("\nBooks in Library 'Central Library':")
    for book in books_in_library("Central Library"):
        print(f"- {book.title}")

    print("\nLibrarian for 'Central Library':")
    librarian = librarian_for_library("Central Library")
    if librarian:
        print(f"- {librarian.name}")