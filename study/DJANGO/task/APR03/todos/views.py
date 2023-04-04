from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

def todo(request):
    todos = Todo.objects.order_by('deadline')

    context = {
        'todos': todos,
    }
    return render(request, 'todos/todo.html', context)

def detail(request,pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo' : todo,
    }
    return render(request, 'todos/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm()
    context = {
        'form' :form,
    }
    return render(request, 'todos/create.html', context)

def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect("todos:todo")

def edit(request, pk):
    if request.method == 'POST':
        todo = Todo.objects.get(pk=pk)
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            todo = form.save(commit=False)
            if request.POST.get('imgfile',True):
                todo.imgfile = request.FILES['imgfile']
            todo.save()
            return redirect('todos:detail', todo.pk)
    else:
        todo = Todo.objects.get(pk=pk)
        form = TodoForm(instance=todo)
    context = {
        'todo': todo,
        'form' : form,
    }
    return render(request, 'todos/edit.html', context)