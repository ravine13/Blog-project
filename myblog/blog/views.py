from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm,UserRegistrationForm
from django.core.paginator import Paginator
from django.contrib.auth import login,authenticate
from .forms import PostForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def home(request):
    posts = Post.objects.all()  
    form = PostForm(request.POST or None) 

    if request.method == "POST" and form.is_valid():
        new_post = form.save(commit=False)
        new_post.author = request.user  
        new_post.save()
        return redirect('/')  

    return render(request, 'blog/home/home.html', {
        'posts': posts,
        'form': form,
    })


def dashboard(request):
    posts = Post.objects.all() 
    return render(request, 'blog/user/dashboard.html')

@login_required
def profile(request):
    return render(request, 'blog/user/profile.html', {'user': request.user})

def user_logout(request):
    logout(request)
    return redirect('login')


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
            return redirect('post_detail', post_id=post.id)  
    else:
        form = CommentForm()
    comments = post.comments.all()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'comments': comments})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('post_list') 
    else:
        form = UserRegistrationForm()

    return render(request, 'blog/registration/register.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.save()
            return redirect('post_list')  
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/') 
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/registration/login.html', {'form': form})

@login_required
def write_story(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.save()
            return redirect('post_list')  
    else:
        form = PostForm()
    
    return render(request, 'blog/write.html', {'form': form})


