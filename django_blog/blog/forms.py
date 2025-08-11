from django import forms # Import the forms module from Django
from django.contrib.auth.models import User # Import the User model
from django.contrib.auth.forms import UserCreationForm # Import the UserCreationForm

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
