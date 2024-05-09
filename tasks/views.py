from django.shortcuts import render
from .models import Task

def home(req):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(req, "tasks/home.html", context)

def undone(req):
    tasks = Task.objects.all().filter(done=False)
    context = {"tasks": tasks}
    return render(req, "tasks/home.html", context)

def done(req):
    tasks = Task.objects.all().filter(done=True)
    context = {"tasks": tasks}
    return render(req, "tasks/home.html", context)

def new(req):
    return render(req, "tasks/new.html")

def detail(req, pk):
    task = Task.objects.get(pk=pk)
    context = {"task": task}
    return render(req, "tasks/detail.html", context)

def edit(req, pk):
    task = Task.objects.get(pk=pk)
    context = {"task": task}
    return render(req, "tasks/edit.html", context)

def delete(req, pk):
    return render(req, "tasks/delete.html")
