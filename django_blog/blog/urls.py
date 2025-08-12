from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentDeleteView, CommentUpdateView

urlpatterns = [
    path('register/', views.register_view, name='register'),  # URL for user registration
    path('profile/', views.profile_view, name='profile'),  # URL for user profile

    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),  # URL for user login
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'), # URL for user logout

    # posts list & CRUD
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # comments
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]