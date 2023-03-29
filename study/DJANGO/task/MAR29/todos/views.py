from django.shortcuts import render, get_object_or_404
from .models import Todo

# Create your views here.

def main(request):
    return render(request, 'todos/main.html')

def todo(request):
    todos = Todo.objects.order_by('-deadline')

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

    title = request.GET.get('title')
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')

    todo = Todo(title=title, content=content, priority=priority, deadline=deadline)
    todo.save()
    
    return render(request, 'todos/success.html')

def remove(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return render(request, 'todos/remove.html')

def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo' : todo,
    }
    return render(request, 'todos/edit.html', context)

def update(request, pk):
    todo = Todo.objects.get(pk=pk)

    title = request.GET.get('title')
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')

    todo = Todo(title=title, content=content, priority=priority, deadline=deadline)
    todo.save()

    context = {
        'todo' : todo,
    }

    return render(request, 'todos/update.html', context)