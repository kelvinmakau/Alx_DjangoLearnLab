from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book

#  Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})  # required path

#  Class-based view for library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # required path
    context_object_name = 'library'
