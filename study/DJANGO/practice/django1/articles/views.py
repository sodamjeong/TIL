from django.shortcuts import render

# Create your views here.
# 특정 기능을 수행하는 view 함수를 만듦

def index(request):
    return render(request, 'articles/index.html')