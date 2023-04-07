from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
import os
from django.conf import settings

# Create your views here.
def index(request):
    
    context = {
        'posts': Post.objects.order_by('-pk'),
    }
    return render(request, 'index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form' : form
    }
    return render(request, 'create.html', context)

@login_required
def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
        'like': post.count_likes_user(),
    }
    return render(request, 'detail.html', context)

@login_required
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts:index')

@login_required
def edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        file_change_check = request.POST.get('fileChange', False)
        file_check = request.POST.get('upload_files-clear', False)
        if file_change_check or file_check:
            os.remove(os.path.join(settings.MEDIA_ROOT, post.img_file.path))
        form = PostForm(request.POST, request.FILES, instance=post)
        
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm(instance=post)
    
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'edit.html', context)

    
    
def category(request, subject):
    context = {
        'posts': Post.objects.filter(category=subject).order_by('-pk'),
    }
    return render(request, 'index.html', context)

def likes(request, pk):
    post = Post.objects.get(pk=pk)

    if post.like_users.filter(pk=request.user.pk).exists():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:detail', post.pk)