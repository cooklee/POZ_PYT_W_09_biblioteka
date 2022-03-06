

from django.test import TestCase
from django.test import Client
import pytest

# Create your tests here.
from django.urls import reverse

from b_app.forms import AddPublisherModelForm
from b_app.models import Publisher, Book


@pytest.mark.django_db
def test_index():
    client = Client()
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_booklist_not_login():
    client = Client()
    url = reverse('list_books')
    response = client.get(url)
    assert response.status_code == 302
    url = reverse('login')
    assert response.url.startswith(url)

@pytest.mark.django_db
def test_booklist_login(user):
    client = Client()
    client.force_login(user)
    url = reverse('list_books')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == 0


@pytest.mark.django_db
def test_booklist_login(user, books):
    client = Client()
    client.force_login(user)
    url = reverse('list_books')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(books)
    for book in books:
        assert book in response.context['object_list']


@pytest.mark.django_db
def test_add_publisher_get():
    client = Client()
    url = reverse('add_publisher_model')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], AddPublisherModelForm)

@pytest.mark.django_db
def test_add_publisher_post():
    client = Client()
    url = reverse('add_publisher_model')
    date = {
        'name':'ala',
        'address' : 'poznanska',
        "street" : "poznanska",
        "city" : "bździna dolna",
        'description':'najlepsze wyd na świecie'
    }
    response = client.post(url, date)
    assert response.status_code == 302
    new_url = reverse('list_author')
    assert response.url.startswith(new_url)
    Publisher.objects.get(**date)


@pytest.mark.django_db
def test_book_update_view(books):
    book = books[0]
    client = Client()
    url = reverse('update_book', args=(book.id,))
    data = {
        'title':'?',
        'year':123,
        'author': book.author.id#### TO JEST WAŻNE
    }
    response = client.post(url, data)

    Book.objects.get(title="?")


