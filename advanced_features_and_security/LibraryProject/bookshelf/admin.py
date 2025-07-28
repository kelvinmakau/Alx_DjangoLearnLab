from django.contrib import admin
from .models import Book, Author, Library, Librarian, CustomUser, UserProfile

# Book admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # Removed 'publication_year'
    list_filter = ('author',)           # Removed 'publication_year'
    search_fields = ('title', 'author__name')  # Searching through related author's name

# Register all relevant models
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(CustomUser)
admin.site.register(UserProfile)
