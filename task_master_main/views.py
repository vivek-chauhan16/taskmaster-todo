from django.shortcuts import render
from task_master.models import Task

def home(request):
    tasks =  Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_completed=True)
    total_pending_tasks = tasks.count()
    total_completed_tasks = completed_tasks.count()
    total_tasks = total_pending_tasks + total_completed_tasks
    context = {
        'tasks':tasks,
        'completed_tasks':completed_tasks,
        'total_pending_tasks': total_pending_tasks,
        'total_completed_tasks': total_completed_tasks,
        'total_tasks': total_tasks,
    }
    return render(request, 'home.html', context)