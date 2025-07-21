from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView

# Create your views here. Function based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
