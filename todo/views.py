from django.shortcuts import render

from todo.models import Task
from todo.serializers import TaskSerializer


def home_view(request):
    tasks = Task.objects.all()

    context = {
        'tasks': TaskSerializer(tasks, many=True).data,
    }

    return render(request, 'home.html', context)
