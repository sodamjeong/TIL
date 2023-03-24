from django.db import models

# Create your models here.

class Todo(models.Model):
    # 필드 이름 (변수명) & 데이터 타입(모델 필드 클래스) 
    # & 제약조건(모델 필드 클래스의 키워드 인자)
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True)
    category = models.CharField(max_length=20, default="charField")