from django.shortcuts import render

# Create your views here.

## task 1

import random

def dinner(request):
    foods = ['떡볶이', '마라탕', '피자', '치킨', '햄버거', '부대찌개', '감자탕', '단식', '짜장면', 
            '짬뽕', '초밥', '족발', '곱창', '닭발', '김밥', '삼겹살', '냉면', '회',]
    drinks = ['소주', '맥주', '와인', '보드카', '하이볼', '위스키', '고량주', '콜라', '사이다', '물', '커피',
              '녹차', '우롱차', '우엉차', '히비스커스티', '호박차',]

    food = random.choice(foods)
    drink = random.choice(drinks)

    context = {
        'food' : food,
        'drink' : drink,
    }

    return render(request, 'dinner.html', context)

## task 2

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    data = request.GET.get('content')
    context = {
        'data' : data,
    }
    return render(request, 'catch.html', context)

## task 3

def lotto_create(request):
    return render(request, 'lotto_create.html')

def lotto(request):

    num = request.GET.get('count')
    lst = []

    for i in range(1,int(num)+1):
        lst.append(sorted(random.sample(list(range(1,46)),6)))

    context = {
        'num' : num,
        'lst' : lst,
    }
    return render(request, 'lotto.html', context)