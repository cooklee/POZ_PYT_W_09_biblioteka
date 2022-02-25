from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from accounts.forms import LoginForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
        return render(request, 'form.html', {'form': form})


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('/')





