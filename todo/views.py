from django.shortcuts import render

from todo.models import Task


def home_view(request):
    backlog_tasks = Task.objects.filter(status=Task.Status.BACKLOG)
    todo_tasks = Task.objects.filter(status=Task.Status.TODO)
    in_progress_tasks = Task.objects.filter(status=Task.Status.IN_PROGRESS)
    done_tasks = Task.objects.filter(status=Task.Status.DONE)

    context = {

        'backlog_tasks': backlog_tasks,
        'todo_tasks': todo_tasks,
        'in_progress_tasks': in_progress_tasks,
        'done_tasks': done_tasks,

    }
    return render(request, 'home.html', context)
