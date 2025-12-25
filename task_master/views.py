from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')