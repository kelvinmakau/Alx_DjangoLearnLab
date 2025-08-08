from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
# Import all the views
from .views import (
    BookListView,
    BookDeleteView,
    BookCreateView,
    BookDetailView,
    BookUpdateView
)

# urls for all the views
urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('api-auth-token/', obtain_auth_token, name='api-auth-token') # Get token
]