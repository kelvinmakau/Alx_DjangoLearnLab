from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST) # Create a form instance with POST data
        if form.is_valid():
            user = form.save() # Save the user instance if the form is valid
            login(request, user) # Log in the user after registration
            return redirect('profile') # Redirect to profile page after registration
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form}) # Display the registration form

@login_required
def profile_view(request):
    if request.method == 'POST': # Handle profile update
        request.user.email = request.POST.get('email', request.user.email) # Update email if provided
        request.user.save() # Save the updated user information
        return redirect('profile') # Redirect to the same profile page after saving changes
    return render(request, 'blog/profile.html', {'user': request.user}) # Display user profile information
