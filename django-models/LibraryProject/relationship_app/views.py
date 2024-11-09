from django.shortcuts import render, redirect

# Create your views here.
from relationship_app.models import Book
from django.views.generic import DetailView
from relationship_app.models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # Optional: Customize the context if needed (e.g., to add extra data)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Add books in the library to the context
        return context
    
    # User login view (uses Django's built-in LoginView)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# User logout view (uses Django's built-in LogoutView)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# User registration view (using UserCreationForm)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Create the new user
            messages.success(request, 'Registration successful. You can now log in!')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})