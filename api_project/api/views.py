from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here. 
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializer
    permission_classes = [IsAuthenticated] # Requires authentication

class BookViewSet(viewsets.ModelViewSet): # Provides full CRUD operations (Create, Read, Update, Delete)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Requires authentication