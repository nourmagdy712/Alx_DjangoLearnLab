from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# Query 2: List all books in a specific library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Query 3: Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return librarian

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
    print(f"- {librarian.name}")