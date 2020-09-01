from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


# Create your views here.

def user_registration(req):

    msg =''
    if req.method == 'POST':
        data = req.POST
        try:
            user = User.objects.create_user(
                data.get('username'), data.get('email'), data.get('password'))
            user.first_name = req.POST.get('fname')
            user.last_name = req.POST.get('lname')
            user.save()
            msg = 'Registration Successful...'
            return render(req, 'user/login.html', {'msg': msg})
        except:
            msg = 'Username already taken...'

    return render(req,'user/user.html',{'msg':msg})

def user_login(req):

    msg = ''
    if req.method == 'POST':
        data = req.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('/')
        else:
            msg = 'Username Password incorrect'

    return render(req, 'user/login.html', {'msg': msg})


@login_required
def user_logout(req):
    
    logout(req)
    return redirect('/user/login/')
