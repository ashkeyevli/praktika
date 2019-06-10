import datetime

from django.db import models
from django.db import models
from django.db.models import CharField
from django.template.backends import django
from django.utils.timezone import now


# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.name)

    def tojson(self):
        return '{}'.format(self.name)



class Task(models.Model):
     name = models.CharField(max_length=100)
     created_at = models.DateTimeField(auto_now_add=True, blank=True)
     due_on = models.DateTimeField(datetime.datetime.now,blank=True)
     COMPLETE = 'COMPLETE'
     IN_PROGRESS = 'IN PROGRESS'
     TASK_STATUS_CHOICES = (
         IN_PROGRESS, "IN PROGRESS")
     status = models.CharField(default=IN_PROGRESS, max_length=50)
     task_list = models.ForeignKey(TaskList, on_delete=models.DO_NOTHING)

     def __str__(self):
         return '{}: {}'.format(self.id, self.name)
     def tojson(self):
         return 'id:{} name:{} status:{}'.format(self.id, self.name,self.status)
     def tojson(self):
         return 'id:{}, name:{}, status:{}'.format(self.id, self.name,self.status)

     def tojson2(self):
         return 'id:{},  name:{},  created_at:{},  due_on:{},  status:{}'.format(self.id, self.name,self.created_at,self.due_on, self.status)



     #def __str__(self):
      #  return '{}'.format(self.name)

     #def tojson(self):
      #  return '{}'.format(self.name)




