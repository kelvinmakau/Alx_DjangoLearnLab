from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet, BookCreateList
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book_list'),
    path('books-create', BookCreateList.as_view(), name="book_create_list"),
    path('', include(router.urls)), # CRUD routes via router
    path('api-token-auth/', obtain_auth_token, name='api-auth-token'), # Token endpoint
]