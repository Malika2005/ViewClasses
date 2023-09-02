from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Genre(models.Model):
    genre_name = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.genre_name}'


class Book(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_year = models.IntegerField()
    genre = models.ManyToManyField(Genre, related_name='books')
    rating = models.IntegerField()
    amount_of_views = models.IntegerField(null=True, default=0)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('book_info', args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

