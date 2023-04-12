from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm, CustomPasswordChangeForm
from .models import User

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('reviews:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('reviews:index')

def join(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
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
    return redirect('reviews:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('reviews:index')
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

@login_required
def mypage(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user,
    }
    return render(request, 'mypage.html', context)