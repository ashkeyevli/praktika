from django.urls import path
from api import views
from django.urls import path, include
urlpatterns = [

    path('task_lists/',views.task_lists),
    path('task_lists/1/',views.t1),
    path('task_lists/1/tasks/',views.tasks),
    path('tasks/2/',views.tasks2)
]
