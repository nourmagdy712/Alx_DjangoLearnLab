### CRUD Operations for Books API

1. **GET /api/books/**: List all books (no authentication required).
2. **GET /api/books/<int:pk>/**: Retrieve a single book by its ID (no authentication required).
3. **POST /api/books/create/**: Create a new book (authentication required).
4. **PUT/PATCH /api/books/<int:pk>/update/**: Update an existing book by ID (authentication required).
5. **DELETE /api/books/<int:pk>/delete/**: Delete a book by ID (authentication required).

### Advanced Query Capabilities in the Book API

#### Filtering:
You can filter books by the following fields:
- **title**: Filter by book title (e.g., `/api/books/?title=Harry Potter`).
- **author**: Filter by author's name (e.g., `/api/books/?author=J.K. Rowling`).
- **publication_year**: Filter by publication year (e.g., `/api/books/?publication_year=1997`).

#### Searching:
You can search books by `title` or `author` using the `search` query parameter:
- Example: `/api/books/?search=Harry`

#### Ordering:
You can order the list of books by `title` or `publication_year`. The ordering can be ascending or descending:
- Example: `/api/books/?ordering=title` (ascending order)
- Example: `/api/books/?ordering=-publication_year` (descending order)

By combining filtering, searching, and ordering, you can query the Book API in a variety of ways to find exactly what you're looking for.