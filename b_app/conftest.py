import pytest
from django.contrib.auth.models import User

from b_app.models import Book, Author


@pytest.fixture
def user():
    return User.objects.create_user(username='cooklee', password='vet')


@pytest.fixture
def author():
    return Author.objects.create(first_name='slawek', last_name='bo')


@pytest.fixture
def books(author):
    lst = []
    for i in range(10):
        x = Book.objects.create(
            title=i,
            year=i,
            author=author
        )
        lst.append(x)
    return lst
