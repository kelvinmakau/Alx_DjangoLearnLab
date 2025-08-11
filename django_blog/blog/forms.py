from django import forms # Import the forms module from Django
from django.contrib.auth.models import User # Import the User model
from django.contrib.auth.forms import UserCreationForm # Import the UserCreationForm
from .models import Post # Import the Post model from the current app's models

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add an email field

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Specify the fields to include in the form

    def save(self, commit=True):
        user = super().save(commit=False)  # Create a user instance without saving it yet
        user.email = self.cleaned_data['email']  # Set the email field
        if commit:
            user.save()  # Save the user instance if commit is True
        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Specify the fields to include in the form, automatically excludes 'author' and 'published_date'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}), # TextInput widget for title
            'content': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Write your post content here...'}), # Textarea widget for content
        }