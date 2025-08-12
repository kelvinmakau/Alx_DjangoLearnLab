from django.db import models
from django.contrib.auth.models import User # Import necessary modules
from taggit.managers import TaggableManager # Import TaggableManager for tagging functionality

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
    tags = TaggableManager() # Tags for the post using TaggableManager

    def __str__(self): # String representation of the Post model
        return self.title
    
class Profile(models.Model): # Define a Profile model
    user = models.OneToOneField(User, on_delete=models.CASCADE) # One-to-one relationship with User model
    bio = models.TextField(blank=True) # Optional biography field
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True) # Optional profile picture field

    def __str__(self):
        return self.user.username # String representation of the Profile model
    
class Comment(models.Model): # Define a Comment model
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # Foreign key to Post model
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign key to User model
    content = models.TextField() # Content of the comment
    created_at = models.DateTimeField(auto_now_add=True) # Date when the comment was created
    updated_at = models.DateTimeField(auto_now=True) # Date when the comment was last updated

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}" # String representation of the Comment model
    
    class Meta:
        ordering = ['-created_at'] # Order comments by creation date in descending order