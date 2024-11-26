from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm,UserRegistrationForm
from django.core.paginator import Paginator
from django.contrib.auth import login
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)  # Redirect back to the post detail page
    else:
        form = CommentForm()

    # Fetching comments explicitly for clarity
    comments = post.comments.all()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'comments': comments})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('post_list')  # Redirect to the post list or home page
    else:
        form = UserRegistrationForm()

    return render(request, 'blog/registration/register.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Associate post with the logged-in user
            post.save()
            return redirect('post_list')  # Redirect to the list of posts
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


