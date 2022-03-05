from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class CreateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']
        widgets = {
            'password':forms.PasswordInput
        }

class UpdateUserPermissionForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [ 'username', 'user_permissions',]
        widgets = {
            'user_permissions': forms.CheckboxSelectMultiple
        }
