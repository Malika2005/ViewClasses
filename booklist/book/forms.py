from django import forms
from .models import Book, Author, Genre


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('slug', 'amount_of_views')

class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class GenreModelForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'