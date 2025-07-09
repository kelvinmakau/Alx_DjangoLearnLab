```python
## Create

from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

# <Book: 1984 by George Orwell (1949)>

## Retrieve

from bookshelf.models import Book

book = Book.ojects.get(title="1984")
book.title, book.author, book.publication_year

# ('1984', 'George Orwell', 1949)

## Update
from bookshelf.models import Book

book = Book.ojects.get(title="1984")
book.title = “Nineteen Eighty-Four”
book.save()
book

# <Book: Nineteen Eighty-Four by George Orwell (1949)>

## Delete
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()

# <QuerySet []>