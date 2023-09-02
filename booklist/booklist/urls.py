"""
URL configuration for booklist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StartPageView.as_view(), name='start_page'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<slug:slug>/', BookInfoView.as_view(), name='book_info'),
    path('add_book/', AddBookView.as_view(), name='add_book'),
    path('add_book/add_author', AddAuthorView.as_view(), name='add_author'),
    path('add_book/add_genre', AddGenreView.as_view(), name='add_genre'),
    path('books/<slug:slug>/update', UpdateBookView.as_view(), name='update_book'),
    path('books/<slug:slug>/delete', DeleteBookView.as_view(), name='delete_book'),
]
