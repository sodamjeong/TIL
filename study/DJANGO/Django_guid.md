# Django 개발 환경 설정

### VSCode extension 설치
- Django
- SQLite Viewer
- extension 관련 설정
    - Open User settings (Json)
    ```json
    "files.associations": {
    "**/*.html": "html",
	    "**/templates/**/*.html": "django-html",
    "**/templates/**/*": "django-txt",
    "**/requirements{/**,*}.{txt,in}": "pip-requirements"
  },
  "emmet.includeLanguages": {
    "django-html": "html"
  }
  ```


### 개발 환경 설정
(VSCode terminal || git bash 입력)
1. 가상환경 생성<br>
: python -m venv venv

2. 가상환경 활성화<br>
: source venv/Scripts/acrivate (window 기준)

3. django 설치<br>
: pip install django==설치 버전
(설치 버전 : 3.2.18)
4. 의존성 파일 생성<br>
: pip freeze > requirements.txt
5. .gitignore 설정<br>
: [gitignore.io](https://www.toptal.com/developers/gitignore/) 활용하여 .gitignore 파일 생성하기<br> (검색 입력 예시: Django, Window, VisualStudioCode)
6. git init
7. django 프로젝트 생성<br>
: django-admin startproject firstpjt.
8. 서버 실행<br>
: python manage.py runserver<Br>
링크 ctrl + 클릭 시, 로켓 발사 화면 확인됨.
9. 서버 종료
: ctrl + c

### 앱 생성
1. python manage.py startapp (articles) 
  - 앱의 이름은 '복수형'으로 지정하는 것을 권장
2. settings.py 파일 INSTALLED_APPS = ['앱 이름' 추가]
  - 앱을 생성한 후에 등록 해야 함, 등록 후 생성 불가능

### 모델 생성

1. 앱의 models.py 파일에 테이블이 될 클래스를 기재한다.

```py
# 예시

from django.db import models

# Create your models here.

class Article(models.Model):
    # 필드 이름 (변수명) & 데이터 타입(모델 필드 클래스) 
    # & 제약조건(모델 필드 클래스의 키워드 인자)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
2. python manage.py makemigrations (migrations 폴더 생성, 0001파일 생성됨)
  - 반드시 makemigrations으로 기재 해야함
3. python manage.py migrate (만들어진 설계도 DB 반영) 
  - DB내에 생성 된 테이블을 확인한다.

4. 모델 필드 추가 시 작성한 클래스에 추가 작성, migration 과정 반복
  - 추가하는 필드의 기본 값 설정이 필요한데 터미널에 뜨는 선택지 중
  - 1번은 지금 기본값을 입력 할 수 있는 터미널로 전환
  - 2번은 models.py 파일에서 직접 지정

5. 필드 추가 과정 완료 후 migraions 폴더에 2번째 파일이 생성됨 
  - 추후 문제 발생 시 복구용으로 사용 (git 의 commit과 유사하다.)

6. 생성된 모델을 admin에 등록한다. 앱의 admin.py 파일에 작성

```py
# 예시

from django.contrib import admin
from .models import Article

# Register your models here.

admin.site.register(Article)
```

7. 활성화 한 서버에서 admin 페이지에 테이블 생성 됐는 지 확인.

### 계정 생성

1. python manage.py createsuperuser 
2. 아이디, 비밀번호 설정

- 해당 계정으로 서버의 admin 페이지에 로그인 한다.
