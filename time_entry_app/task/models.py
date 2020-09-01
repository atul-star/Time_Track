from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    project = models.CharField(max_length=255)
    stime = models.DateTimeField()
    etime = models.DateTimeField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='taskref', null=True)
