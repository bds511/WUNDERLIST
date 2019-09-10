from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.

def index(request):
    todos= Todo.objects.all()
    return render(request, 'todos/index.html',{'todos':todos})


def new(request):
    return render(request, 'todos/new.html')

def create(request):
    title=request.POST.get('title')
    due_date=request.POST.get('due-date')
    Todo.objects.create(title=title,due_date= due_date)
    return redirect('todos:index')

def edit(request,pk):
    todo = Todo.objects.get(id=pk)
    return render(request,'todos/edit.html',{'todo':todo})

def update(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.title=request.POST.get('title')
    todo.due_date=request.POST.get('due-date')
    todo.save()
    return redirect('todos:index')

def delete(request,pk):
    Todo.objects.get(id=pk).delete()
    return redirect('todos:index')

