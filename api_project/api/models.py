from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()

    # Returns the real saved book object in the django admin page, instead of Book object(1)
    def __str__(self): 
        return f"{self.title} by {self.author} published on {self.published_date}"
