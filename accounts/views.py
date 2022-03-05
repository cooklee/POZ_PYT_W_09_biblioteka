from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from accounts.forms import LoginForm, CreateUserForm, UpdateUserPermissionForm


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
                redirect_url = request.GET.get('next', '/')
                return redirect(redirect_url)
        return render(request, 'form.html', {'form': form})


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class RegistrationView(View):

    def get(self, request):
        form = CreateUserForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("/")
        return render(request, 'form.html', {'form': form})


class UserPermissionUpdateView(View):

    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        form = UpdateUserPermissionForm(instance=user)
        return render(request, 'form.html', {'form':form})

    def post(self, request, user_id):
        user = User.objects.get(pk=user_id)
        form = UpdateUserPermissionForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return render(request, 'form.html', {'form':form})