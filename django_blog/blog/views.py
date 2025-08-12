from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, PostForm, CommentForm
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy

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

@login_required(login_url='login') # Ensure the user is logged in to access the profile view
def profile_view(request):
    if request.method == 'POST': # Handle profile update
        request.user.email = request.POST.get('email', request.user.email) # Update email if provided
        request.user.save() # Save the updated user information
        return redirect('profile') # Redirect to the same profile page after saving changes
    return render(request, 'blog/profile.html', {'user': request.user}) # Display user profile information

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # blog/templates/blog/post_list.html
    context_object_name = 'posts'  # Name of the variable to access posts in the template
    ordering = ['-published_date']  # Order posts by published date in descending order
    paginate_by = 10 # Number of posts per page

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # blog/templates/blog/post_detail.html
    context_object_name = 'post'  # Name of the variable to access the post in

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Get the default context
        post = self.get_object() # Get the current post object
        context['comments'] = post.comments.all() # Get all comments related to the post
        context['comment_form'] = CommentForm()

        return context  # Return the updated context
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        self.object = self.get_object()  # Get the current post object
        form = CommentForm(request.POST)  # Create a form instance with POST data
        if form.is_valid():
            comment = form.save(commit=False)  # Create a comment instance without saving it yet
            comment.post = self.object  # Set the post for the comment
            comment.author = request.user  # Set the author of the comment to the logged-in user
            comment.save()  # Save the comment instance
            return redirect('post-detail', pk=self.object.pk)  # Redirect to the post detail page
        
        # If the form is not valid, render the post detail page with the form errors
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)  # Render the post detail page with the form errors
            

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm # Use the PostForm defined in forms.py
    template_name = 'blog/post_form.html'  # blog/templates/blog/post_form.html

    def form_valid(self, form): # Override form_valid to set the author
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)  # Call the parent class's form_valid method
    
    def get_success_url(self):  # Redirect to the post detail page after creation
        return reverse('post-detail', kwargs={'pk': self.object.pk})  # Redirect to the newly created post
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm  # Use the PostForm defined in forms.py
    template_name = 'blog/post_form.html'  # blog/templates/blog/post_form.html
    login_url = 'login'  # Redirect to login page if not logged in

    def test_func(self):  # Ensure only the author can update the post
        post = self.get_object()
        return self.request.user == post.author
    
    def get_success_url(self):  # Redirect to the post detail page after creation
        return reverse('post-detail', kwargs={'pk': self.object.pk})  # Redirect to the newly created post
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # blog/templates/blog/post_confirm_delete.html
    success_url = reverse_lazy('post-list')  # Redirect to posts page after deletion
    login_url = 'login'  # Redirect to login page if not logged in

    def test_func(self):  # Ensure only the author can delete the post
        post = self.get_object()
        return self.request.user == post.author
    
# Edit and delete views for comments
class CommentCreateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm  # CommentForm in forms.py
    template_name = 'blog/comment_form.html'  # blog/templates/blog/comment_form.html

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})  # Redirect to the post detail page after updating
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author # Ensure only the author can update the comment
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'  # blog/templates/blog/comment_confirm_delete.html

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.pk}) # Redirect to the post detail page after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
