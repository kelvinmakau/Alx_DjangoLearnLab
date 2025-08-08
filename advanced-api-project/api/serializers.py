from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year']

    def validate_publication_year(self, value):
        current_year = datetime.now().year

        # Validate that the publication year is not in the future
        if value > current_year:
            raise serializers.ValidationError("Publiction year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) # Nested serialized of books
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
