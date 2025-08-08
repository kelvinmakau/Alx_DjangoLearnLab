from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
# ListView for retrieving all books - ReadOnly
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] # Anyone can read

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
