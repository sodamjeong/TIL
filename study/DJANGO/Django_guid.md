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