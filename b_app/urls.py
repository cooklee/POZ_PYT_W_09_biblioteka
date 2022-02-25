"""biblioteczka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from b_app import views

urlpatterns = [
    path("add_author/", views.AuthorAddView.as_view(), name='add_author'),
    path("author_list/", views.AuthorListView.as_view(), name='list_author'),
    path("author_detail/<int:id>/", views.AuthorDetail.as_view(), name='detail_author'),
    path("add_book/", views.AddBook.as_view(), name='add_book'),
    path("add_publisher/", views.AddPublisherView.as_view(), name='add_publisher'),
    path("add_publisher_model/", views.AddPublisherFormModelView.as_view(), name='add_publisher_model'),
    path("create_publisher/", views.AddPublisherCreateView.as_view(), name='create_publisher'),
    path("list_book/", views.BookListView.as_view(), name='list_books'),
    path("list_user/", views.UserListView.as_view(), name='list_users'),
    path("update_book/<int:pk>/", views.BookUpdateView.as_view(), name='update_book'),
]
