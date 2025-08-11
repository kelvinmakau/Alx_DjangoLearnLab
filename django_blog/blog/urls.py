from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('register/', views.register_view, name='register'),  # URL for user registration
    path('profile/', views.profile_view, name='profile'),  # URL for user profile

    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),  # URL for user login
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'), # URL for user logout

    # posts list & CRUD
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]