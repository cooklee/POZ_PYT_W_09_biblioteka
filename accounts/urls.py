from django.urls import path

from accounts import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name='login'),
    path("logout/", views.LogOut.as_view(), name='logout')
]
