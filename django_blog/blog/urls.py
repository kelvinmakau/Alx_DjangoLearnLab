from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),  # URL for user registration
    path('profile/', views.profile_view, name='profile'),  # URL for user profile

    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),  # URL for user login
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'), # URL for user logout
]