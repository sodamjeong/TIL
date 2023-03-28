from django.db import models

class Math:
    number = 3

    def __init__(self, a, b):
        pass

    def add(self):
        pass
a = Math()

result = a.add()

a = []

b = list()

a.append(1)

class list:
    def append(self, *args):
        pass



class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Article 클래스의 인스턴스 생성
article = Article()

# article 인스턴스에 title과 content 인스턴스 변수에 값을 저장
article.title = '제목'
article.content = '내용'

# 테이블에 레코드 하나 생성을 위해 저장 (인스턴스 메서드 save 호출)
article.save()

# 생성 2번째 방법
article = Article(title='second', content='django!')
article.save()

# 3번째 방법 (QuerySet API중에 create 메서드를 활용)
Article.objects.create(title='third', content='django!')