from django.db import models
from django.contrib.auth.models import User # Import necessary modules

# Create your models here.
class Post(models.Model): # Define a Post model
    title = models.CharField(max_length=200) # Title of the post
    content = models.TextField() # Content of the post
    published_date = models.DateTimeField(auto_now_add=True) # Date when the post was published
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def __str__(self): # String representation of the Post model
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # One-to-one relationship with User model
    bio = models.TextField(blank=True) # Optional biography field
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True) # Optional profile picture field

    def __str__(self):
        return self.user.username # String representation of the Profile model