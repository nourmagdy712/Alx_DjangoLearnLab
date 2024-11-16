from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

class ExampleForm(forms.Form):
    # Define your form fields here
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)

    # You can also add custom validation or widgets
    def clean_title(self):
        title = self.cleaned_data['title']
        if not title.isalpha():
            raise forms.ValidationError("Title should only contain letters")
        return title