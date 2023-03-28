# 모델 참고

from django.db import models

class Todo(models.Model):
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True)



# 1.

todo = Todo()

todo.content = '실습 제출'
todo.priority = '5'
completed = 'False'
todo.deadline = '2023-03-28'
todo.save()

# 2. 

todo.content = '데일리 설문(오후) 제출'
todo.deadline = '2023-03-28'
todo.save()

# 3.

todo = Todo(content='퇴실 QR 찍기', deadline = '2023-03-28')
todo.save()
Todo.objects.create(content='산책 가기', priority = '6', deadline = '2023-03-28')
Todo.objects.create(content='약 먹기', priority = '7', deadline = '2023-03-28')
Todo.objects.create(content='저녁 먹기', priority = '8', deadline = '2023-03-28')
Todo.objects.create(content='공부 하기', priority = '9', deadline = '2023-03-28')

# 4. 

Todo.objects.all().order_by('pk')

# 5.

Todo.objects.all().order_by('-priority')

# 6.

print(Todo.objects.get(pk=1).content)
print(Todo.objects.get(pk=1).priority)
print(Todo.objects.get(pk=1).deadline)
print(Todo.objects.get(pk=1).created_at)

# 6-1.
num1 = Todo.objects.get(pk=1)
print(num1.content, num1.priority, num1.deadline, num1.created_at)



