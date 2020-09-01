from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from task.models import Task
from datetime import datetime, date, time
import pytz


@login_required
def task_home(req):
    msg = ''
    return render(req, 'task/task_home.html', {'msg': msg})


@login_required
def add_task(req):

    msg = ''
    if req.method == 'POST':
        data = req.POST
        if data.get('project') == '':
            msg = 'Please choose project...'
            return render(req, 'task/add_task.html', {'msg': msg})
        elif data.get('stime') >= data.get('etime'):
            msg = 'Start time cant be less than or equal to end time'
            return render(req, 'task/add_task.html', {'msg': msg})
        else:
            s = str(data.get('stime')).split(sep=':')
            e = str(data.get('etime')).split(sep=':')

            stm = time(int(s[0]), int(s[1]), 0)
            etm = time(int(e[0]), int(e[1]), 0)
            try:
                msg = 'Task Added Successfully..'
                task_obj = Task.objects.create(task_name=data.get(
                    'task_name'), project=data.get('project'),
                    stime=datetime.combine(date.today(), stm),
                    etime=datetime.combine(date.today(), etm),
                    user=req.user)
                task_obj.save()
            except:
                msg = 'Error while saving task... please try after some time'
                return render(req, 'task/add_task.html', {'msg': msg})

            return render(req, 'task/task_home.html', {'msg': msg})

    return render(req, 'task/add_task.html', {'msg': msg})


@login_required()
def task_task(req):
    flag = False
    utc = pytz.UTC
    msg = ''

    task = Task.objects.filter(user=req.user).last()
     
    if task:
        if task.etime < utc.localize(datetime.now()):
            msg = 'You dont have running task to show...'
            return render(req, 'task/task_track.html', {'task': task, 'msg': msg,
                                                        'date': task.etime, 'flag': flag})
        elif task.stime > utc.localize(datetime.now()):
            msg = 'Your task doesnt start yet...'
            return render(req, 'task/task_track.html', {'task': task, 'msg': msg,
                                                        'date': task.etime, 'flag': flag})
        else:
            flag = True
            msg = 'Here your task '

        return render(req, 'task/task_track.html', {'task': task, 'msg': msg,
                                                    'date': task.etime, 'flag': flag})
    msg = 'zero task to show..'
    return render(req, 'task/task_track.html', {'task': '', 'msg': msg,
                                                'date': '', 'flag': flag})

@login_required
def task_list(req):
    msg = ''
    task_obj = Task.objects.filter(user=req.user).all()
    if task_obj:
        msg='Your task are as follow:'
        return render(req, 'task/task_list.html',{'msg':msg, 'tasklist':task_obj})

    msg = 'Zero task to show...'
    return render(req, 'task/task_list.html',{'msg':msg, 'tasklist':task_obj})
    
