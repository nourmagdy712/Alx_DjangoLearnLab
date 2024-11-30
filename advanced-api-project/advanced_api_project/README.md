### CRUD Operations for Books API

1. **GET /api/books/**: List all books (no authentication required).
2. **GET /api/books/<int:pk>/**: Retrieve a single book by its ID (no authentication required).
3. **POST /api/books/create/**: Create a new book (authentication required).
4. **PUT/PATCH /api/books/<int:pk>/update/**: Update an existing book by ID (authentication required).
5. **DELETE /api/books/<int:pk>/delete/**: Delete a book by ID (authentication required).