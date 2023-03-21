# Django design pattern

## 1. Project & App 
- Django project : 애플리케이션의 집합 (DB 설정, URL 연결, 전체 앱 설정 등을 처리)
- Django application : 독립적으로 작동하는 기능 단위 모듈<br>(각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성)

## 2. 디자인 패턴
- 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책<br>(공통적인 문제를 해결하는데 쓰이는 형식화 된 관행)

### MVC 디자인 패턴
- Model - View - Controller
- 애플리케이션을 구조화하는 대표적인 패턴 (데이터, 사용자 인터페이스, 비즈니스 로직을 분리)
    - 시각적 요소, 뒤에서 실행되는 로직을 서로 영향 없이 독립적이고 유지보수가 쉬운 애플리케이션을 만들기 위해

### MTV 디자인 패턴
- Model - Template - View
- django에서 애플리케이션을 구조화하는 패턴 (MVC 패턴과 동일하나 명칭을 다르게 정의했다.)
- View -> Template, Controller -> View

### 프로젝트 구조
- settings.py : 프로젝트의 모든 설정을 관리
- urls.py : URL과 이에 해당하는 적절한 views를 연결
- ```__init__```.py : 해당 폴더를 패키지로 인식하도록 설정
- asgi.py : 비동기식 웹 서버와의 연결 관련 설정
- wsgi.py : 웹 서버와의 연결 관련 설정
- manage.py : Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

### 앱 구조
- admin.py : 관리자용 페이지 설정
- models.py : DB와 관련된 Model을 정의, ```MTV패턴의 M```
- views.py : HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환 (url, mode, template과 연계) ```MTV 패턴의 V```
- apps.py : 앱의 정보가 작성된 곳
- tests.py : 프로켁트 테스트 코드를 작성하는 곳

## 3. 요청과 응답

### URLs

```py
from django.contrib import admin
from django.urls import path

# articles 패키지에서 views 모듈을 가져와야 함
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.index)
]
```
- http://128.0.0.1:8000/articles/ 로 요청이 왔을 때 views 모듈의 index 뷰 함수를 호출한다는 의미

### View
```py
from django.shortcuts import render

# Create your views here.
# 특정 기능을 수행하는 view 함수를 만듦

def index(request):
    return render(request, 'articles/index.html')
```
- 특정 경로에 있는 template과 request 객체를 결합해 응답 객체를 반환하는 index 뷰 함수 정의

### Template
```py
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello, Django!</h1>
</body>
</html>
```
- articles 앱 폴더안에 templates 폴더를 생성(반드시 templates 여야함)
- templates 폴더 안에 템플릿 페이지 작성
- django 에서 template을 인식하는 경로 규칙
    - app폴더 / templates / 까지 기본 경로로 인식
    - 해당 지점 이후의 template 경로를 작성해야 함.