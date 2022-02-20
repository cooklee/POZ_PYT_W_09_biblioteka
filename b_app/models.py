from django.db import models

# Create your models here.
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('detail_author', args=(self.id,))


class Book(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

