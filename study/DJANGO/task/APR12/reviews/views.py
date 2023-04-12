from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm,CommentForm
from .models import Review,Comment
import os
from django.conf import settings

# Create your views here.
def index(request):
    context = {
        'reviews': Review.objects.order_by('-pk'),
    }
    return render(request, 'index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form' : form
    }
    return render(request, 'create.html', context)

@login_required
def detail(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        'review': review,
        'comment_form' : comment_form,
        'comments' : comments,
        'like': review.count_likes_user(),
    }
    return render(request, 'detail.html', context)

@login_required
def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:
        review.delete()
    return redirect('reviews:index')

@login_required
def edit(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                review = form.save()
                return redirect('reviews:detail', review.pk)
        else:
            form = ReviewForm(instance=review)
    else:
        return redirect('reviews:detail', review.pk)
    context = {
        'review': review,
        'form' : form,
    }
    return render(request, 'edit.html', context)

def likes(request, pk):
    review = Review.objects.get(pk=pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('reviews:detail', review.pk)

@login_required
def comment_create(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('reviews:detail', review.pk)
    context = {
        'review' : review,
        'comment_form' : comment_form,
    }
    return render(request, 'detail.html', context)

@login_required
def comment_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('reviews:detail', pk)