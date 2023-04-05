from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomAuthenticationForm, CustomUserChangeForm, CustomUserCreationForm, CustomPasswordChangeForm
# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('main')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('main')      
    else:
        form = CustomAuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('main')

def join(request):
    if request.user.is_authenticated:
        return redirect('main')
       
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/join.html', context)

def withdraw(request):
    request.user.delete()
    auth_logout(request)
    return redirect('main')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html',context)

def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomPasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)

def mypage(request, pk):
    user = User.objects.get(pk=pk)
    context ={
        'user' : user
    }
    return render(request, 'accounts/mypage.html', context)