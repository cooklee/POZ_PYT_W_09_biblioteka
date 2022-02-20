

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from b_app.forms import AddBookForm
from b_app.models import Author, Book


class Index(View):
    def get(self, request):
        return render(request, "index.html", )


class AuthorAddView(View):
    def get(self, request):
        return render(request, 'add_author.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Author.objects.create(first_name=first_name, last_name=last_name)

        return redirect(reverse('add_author'))



class AuthorListView(View):
    def get(self, request):
        authors =Author.objects.all()
        return render(request, 'author_list.html', {'authors':authors})


class AuthorDetail(View):

    def get(self, request, id):
        author = Author.objects.get(id=id)
        return render(request, 'author.html', {'author':author})


class AddBook(View):

    def get(self, request):
        form = AddBookForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = AddBookForm(request.POST)
        print("id authora którego przesyłąm to ", request.POST['author'])
        if form.is_valid():
            title = form.cleaned_data['title']
            year = form.cleaned_data['year']
            author = form.cleaned_data['author']
            Book.objects.create(title=title, year=year, author=author)
            return redirect('add_book')
        return render(request, 'form.html', {'form':form})


