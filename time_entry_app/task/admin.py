from django.contrib import admin
from task.models import Task
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','task_name', 'project', 'stime', 'etime', 'user']


admin.site.register(Task, TaskAdmin)
