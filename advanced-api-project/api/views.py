from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend # to add filters and ordering
from django_filters import rest_framework
from rest_framework import filters

# Create your views here.
# ListView for retrieving all books - ReadOnly
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] # Anyone can read

    #to add filters, searching and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # search fields
    search_fields = ['title', 'author__name'] # double underscore for related names

    # ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] # default ordering

# Retrieve a single book by ID ReadOnly
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create a new book, only authenticated users    
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # User must be authenticated

    # custom assigns the current user as creator when book is created
    def perform_create(self, serializer):
        # Save the book
        serializer.save()

# Update book details, must be authenticated
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Must be authenticated/logged in

# Delete an existing book. Must be authenticated
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Must be authenticated/logged in
