from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm,CommentForm
from .models import Article,Comment, Emote
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    articles =  Article.objects.order_by('-pk')
    page = request.GET.get('page', '1')
    per_page = 4
    paginator = Paginator(articles, per_page)
    page_obj = paginator.get_page(page)

    context = {
        'articles': page_obj,
    }
    return render(request, 'index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'create.html', context)

EMOTIONS = [
    {'label': '😆', 'value': 1},
    {'label': '😑', 'value': 2},
    {'label': '😡', 'value': 3},
]


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.order_by('-pk')

    emotions = []
    for emotion in EMOTIONS:
        label = emotion['label']
        value = emotion['value']
        count = Emote.objects.filter(article=article, emotion=value).count()
        if request.user.is_authenticated:
            exist = Emote.objects.filter(article=article, emotion=value, user=request.user)
        else:
            exist = None
        emotions.append(
            {
                'label': label,
                'value': value,
                'count': count,
                'exist': exist,
            }
        )

    context = {
        'emotions': emotions,
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments,
        'like': article.count_likes_user(),
    }
    return render(request, 'detail.html', context)

@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')

@login_required
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                article = form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'edit.html', context)

def likes(request, pk):
    article = Article.objects.get(pk=pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:detail', article.pk)

@login_required
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    comments = article.comment_set.order_by('-pk')
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article' : article,
        'comment_form' : comment_form,
        'comments' : comments,
        'like': article.count_likes_user(),
    }
    return render(request, 'detail.html', context)

@login_required
def comment_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', pk)


def comment_likes(request, pk, comment_pk):
    article = Article.objects.get(pk=pk)
    comment = Comment.objects.get(pk=comment_pk)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    return redirect('articles:detail', article.pk)

@login_required
def emotes(request, pk, emotion):
    article = Article.objects.get(pk=pk)
    filter_query = Emote.objects.filter(
        article=article,
        user=request.user,
        emotion=emotion,
    )
    if filter_query.exists():
        filter_query.delete()
    else:
        Emote.objects.create(article=article, user=request.user, emotion=emotion)

    return redirect('articles:detail',pk)