```python

from bookshelf.models import Book
book = Book.ojects.get(title="1984")
book.title, book.author, book.publication_year

# ('1984', 'George Orwell', 1949)