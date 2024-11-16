# Django Application with Custom Permissions and Groups

This Django application demonstrates how to set up groups and permissions to restrict access to certain parts of the application.

## Steps to Implement

1. **Custom Permissions**:
   - `can_view`: Permission to view books.
   - `can_create`: Permission to create books.
   - `can_edit`: Permission to edit books.
   - `can_delete`: Permission to delete books.

2. **Groups**:
   - **Viewers**: Can view books.
   - **Editors**: Can view, create, and edit books.
   - **Admins**: Can view, create, edit, and delete books.

3. **Enforcing Permissions in Views**:
   - Use the `@permission_required` decorator to restrict access to views based on the permissions defined in `book_app` model.

4. **Testing**:
   - Create users and assign them to different groups using Django Admin or the shell.
   - Test by logging in as different users and verifying access to various views.