from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST.get('task','').strip()
    if task == "":
        messages.error(request, "❌ Task cannot be empty!", extra_tags='add_error')
        return redirect('home')
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

def edit_task(request,pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        new_task = request.POST.get('task', '').strip()

        if new_task == "":
            messages.error(request,"❌ Task cannot be empty!")
            return redirect("edit_task",pk=pk)

        get_task.task = new_task
        get_task.save()
        messages.success(request, "✅ Task updated successfully!", extra_tags='update_success')
        return redirect('home')
    else:
        context={
            'get_task': get_task,
        }
        return render(request, 'edit_task.html', context)
    