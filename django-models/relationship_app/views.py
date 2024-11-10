from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def list_books(request):
    books = Book.objects.all() 
    context = {'book_list': books} 
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['book'] = self.object.books.all()
        return context
"""
    # View for login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home or another page after login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

# View for logout
def user_logout(request):
    logout(request)
    return render(request, 'logout.html')

# View for registration
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
# Example of a protected view
@login_required
def home(request):
    return render(request, 'home.html')

"""

# View for registration
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Example of a protected view (only accessible by logged-in users)
@login_required
def home(request):
    return render(request, 'home.html')