from django.db import models
from datetime import datetime

# Create your models here.
class Author(models.Model): # Author model
    name = models.CharField(max_length=100) # Author name

    def __str__(self):
        return self.name

class Book(models.Model): # Book model
    title = models.CharField(max_length=100) # Title of the book
    publication_year = models.IntegerField() # Date published
    # Foreign key linking to Author model
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} on {self.publication_year} by {self.author}"
