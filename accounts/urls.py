from django.urls import path

from accounts import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name='login'),
    path("logout/", views.LogOut.as_view(), name='logout'),
    path("registration/", views.RegistrationView.as_view(), name='registration'),
    path("set_permission/<int:user_id>/", views.UserPermissionUpdateView.as_view(), name='set_permission')

]
