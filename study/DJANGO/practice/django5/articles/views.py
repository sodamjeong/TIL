from django.shortcuts import render, redirect
from .models import Article


# Create your views here.

def index(request):
    # DB에 전체 게시글 조회를 요청
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # new에서 보낸 사용자 데이터를 받아서 변수에 할당
    # print(request.GET)
    title = request.POST['title']
    content = request.POST['content']

    # 받은 데이터를 DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    # 저장 전에 유효성 검사와 같은 추가 작업을 위해 2번 방법을 택함
    article = Article(title=title, content=content)
    article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    # 결과 페이지 반환
    # return render(request, 'articles/create.html')


    # 이동 URL 반환
    # return redirect("articles:index")

    # 생성한 글의 단일 조회(Detail) 주소
    return redirect("articles:detail", article.pk)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect("articles:index")

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }

    return render(request,'articles/edit.html', context) 

def update(request, pk):
    article = Article.objects.get(pk=pk)
    title = request.POST['title']
    content = request.POST['content']

    article.title = title
    article.content = content
    article.save()
    
    return redirect("articles:detail", article.pk)