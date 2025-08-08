from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(title="Book A", author=self.author1, publication_year=2020)
        self.book2 = Book.objects.create(title="Book B", author=self.author2, publication_year=2021)

        self.list_url = reverse('book-list')     
        self.create_url = reverse('book-create') 

    def test_create_book(self):
        """Ensure we can create a new book"""
        data = {
            "title": "Book C",
            "author": self.author1.id,  # Using ID for FK
            "publication_year": 2022
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.latest('id').title, "Book C")

    def test_list_books(self):
        """Ensure we can list books"""
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_update_book(self):
        """Ensure we can update a book"""
        url = reverse('book-detail', args=[self.book1.id])  # Adjust to your view name
        data = {"title": "Updated Title", "author": self.author1.id, "publication_year": 2020}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        """Ensure we can delete a book"""
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_filter_books_by_author(self):
        """Ensure filtering by author works"""
        response = self.client.get(f"{self.list_url}?author={self.author1.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book['author'] == self.author1.id for book in response.data))

    def test_search_books_by_title(self):
        """Ensure searching by title works"""
        response = self.client.get(f"{self.list_url}?search=Book A")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Book A" in book['title'] for book in response.data))

    def test_order_books_by_year(self):
        """Ensure ordering works"""
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))

    def test_permission_required_for_create(self):
        """Ensure unauthenticated users cannot create a book"""
        self.client.logout()
        data = {"title": "Book D", "author": self.author1.id, "publication_year": 2022}
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
