# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment, LikeBlog
from .forms import BlogForm  # Create this form using `django.forms.ModelForm`
from rest_framework import viewsets
from .serializers import BlogSerializer
from .serializers import CommentSerializer, CommentCreateSerializer, LikeBlogSerializer, LikeBlogCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

@login_required
def homepage(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog/homepage.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)  # Include request.FILES to handle image uploads
        if form.is_valid():
            form.save()
            return redirect('blog-homepage')
    else:
        form = BlogForm()

    return render(request, 'blog/blog_create.html', {'form': form})
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        # Include request.FILES to handle file uploads
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog-homepage')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blog_form.html', {'form': form, 'form_title': 'Edit Blog'})

def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog-homepage')
    return render(request, 'blog/blog_confirm_delete.html', {'blog': blog})

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_class(self):
            if self.request.method == 'GET':
                return CommentSerializer
            elif self.request.method == 'POST':
                return CommentCreateSerializer

class LikeBlogViewSet(viewsets.ModelViewSet):
    queryset = LikeBlog.objects.all()
    serializer_class = LikeBlogSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LikeBlogSerializer
        elif self.request.method == 'POST':
            return  LikeBlogCreateSerializer


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("blog-homepage")
        else:
            return render(request, "blog/login.html", {"error": "Invalid username or password"})
    return render(request, "blog/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "blog/register.html", {"form": form})