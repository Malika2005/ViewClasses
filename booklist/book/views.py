from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *
from .models import *


class StartPageView(TemplateView):
    template_name = 'start_page.html'


class BookListView(ListView):
    template_name = 'book_list.html'
    model = Book
    context_object_name = 'books'


class BookInfoView(DetailView):
    template_name = 'book_info.html'
    model = Book
    context_object_name = 'book'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.amount_of_views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class AddBookView(CreateView):
    template_name = 'add_book.html'
    model = Book
    form_class = BookModelForm
    success_url = reverse_lazy('book_list')

class AddAuthorView(CreateView):
    template_name = 'add_author.html'
    model = Author
    form_class = AuthorModelForm
    success_url = reverse_lazy('add_book')

class AddGenreView(CreateView):
    template_name = 'add_genre.html'
    model = Genre
    form_class = GenreModelForm
    success_url = reverse_lazy('add_book')


class UpdateBookView(UpdateView):
    template_name = 'update_book.html'
    model = Book
    form_class = BookModelForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteBookView(DeleteView):
    template_name = 'delete_book.html'
    model = Book
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('book_list')
