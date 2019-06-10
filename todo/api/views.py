from django.http import HttpResponse,JsonResponse
from api.models import TaskList

from django.shortcuts import render


# Create your views here.
def task_lists(request):
    name= TaskList.objects.all()
    jsonTasklist=[c.tojson() for c in name]
    data={
        'name':jsonTasklist
    }
    return JsonResponse(data,safe=False)

def t1(request):
    name= TaskList.objects.get(id=3)

    data={

        'name':name.tojson()
    }
    return JsonResponse(data,safe=False)
def tasks(request):
    List= TaskList.objects.get(id=1)
    task= List.task_set.all()

    jsonTasks=[c.tojson() for c in task]

    return JsonResponse(jsonTasks,safe=False)
def tasks2(request):
    List= TaskList.objects.get(id=1)
    task= List.task_set.all()

    jsonTasks=[c.tojson2() for c in task]

    return JsonResponse(jsonTasks,safe=False)