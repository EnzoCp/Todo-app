from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import AddForm


# Create your views here.


def home(request):
    todos = Todo.objects.all()
    data = {'todos': todos}
    return render(request, 'todos/home.html', data)


def addtodo(request):
    form = AddForm()
    if request.method == "POST":
        try:
            form = AddForm(request.POST)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'todos/add.html', {'error': "Bad data!"})

    data = {'form': form}
    return render(request, 'todos/add.html', data)


def edittodo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'GET':
        form = AddForm(instance=todo)
        return render(request, 'todos/edittodo.html', {'form': form, 'todo': todo})
    else:
        try:
            form = AddForm(request.POST, instance=todo)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'todos/edittodo.html', {'form': form, 'error': "Bad data!", 'todo': todo})


def deletetodo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == "POST":
        todo.delete()
        return redirect('home')
