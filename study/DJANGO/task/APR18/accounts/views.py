
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm, CustomPasswordChangeForm
from django.contrib.auth import get_user_model
# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def join(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'join.html', context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile',request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'update.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomPasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'change_password.html', context)

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    total_likes = person.like_articles.all().count() + person.like_comments.all().count()
    context = {
        'person' : person,
        'total_likes' : total_likes,
    }
    return render(request, 'profile.html', context)


@login_required
def follow(request, username):
    User = get_user_model()
    you = User.objects.get(username=username)
    me = request.user
    if you != me:
        if me in you.followers.all():
            you.followers.remove(me)
        else:
            you.followers.add(me)
    return redirect('accounts:profile', you.username)
