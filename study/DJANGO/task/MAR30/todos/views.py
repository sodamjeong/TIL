from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def main(request):
    return render(request, 'todos/main.html')

def todo(request):
    todos = Todo.objects.order_by('deadline')

    context = {
        'todos' : todos,
    }
    return render(request, 'todos/todos.html', context)

def todocontent(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo' : todo,
    }
    return render(request, 'todos/todocontent.html', context)

def create(request):
    return render(request, 'todos/create.html')

def success(request):

    title = request.POST['title']
    content = request.POST['content']
    completed = request.POST.get('completed', False) == 'on'
    priority = request.POST['priority']
    deadline = request.POST['deadline']

    todo = Todo(title = title, content = content, completed = completed, priority = priority, deadline = deadline)
    todo.save()
    
    return redirect("todos:todocontent", todo.pk)

def remove(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect("todos:todo")


def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo' : todo,
    }

    return render(request, 'todos/edit.html', context) 

def update(request, pk):
    todo = Todo.objects.get(pk=pk)

    todo.title = request.POST['title']
    todo.content = request.POST['content']
    todo.completed = request.POST.get('completed', False) == 'on'
    todo.priority = request.POST['priority']
    todo.deadline = request.POST['deadline']

    todo.save()
    
    return redirect("todos:todocontent", todo.pk)