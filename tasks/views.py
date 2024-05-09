from django.shortcuts import render


def home(req):
    return render(req, "tasks/home.html")

def new(req):
    return render(req, "tasks/new.html")

def undone(req):
    return render(req, "tasks/undone.html")

def done(req):
    return render(req, "tasks/done.html")

def detail(req):
    return render(req, "tasks/detail.html")

def delete(req):
    return render(req, "tasks/delete.html")
