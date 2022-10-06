from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task
from django.contrib.auth.models import User

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    finished_task = 0
    notfinished_task = 0
    message = ""

    data_task = Task.objects.filter(user=request.user).all()
    for task in data_task:
        if (task.is_finished):
            finished_task += 1
        else:
            notfinished_task += 1

    if (finished_task >= notfinished_task and (finished_task + notfinished_task != 0)):
        message = "Wow, you're doing great! ♡ ´･ᴗ･ `♡"
    else:
        message = "Keep going ฅ^•ﻌ•^ฅ..."

    context = {
    'list_task': data_task,
    'message': message,
    }
    return render(request, "todolist.html", context)

def status(request, id):
    status = Task.objects.get(pk=id)
    if status.is_finished:
        status.is_finished = False
    else:
        status.is_finished = True
    status.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def delete(request, id):
    delete = Task.objects.get(pk=id)
    delete.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def username_clean(request, username):  
    username = username.lower()  
    new = User.objects.filter(username = username)  
    if new.count():
        messages.info(request, "User already exist")
        return None 
    return username

def clean_password2(request, password1, password2):   
    if password1 and password2 and password1 != password2:
        messages.info(request, "Password don't match")
        return None  
    return password2

def register(request):
    if request.method == "POST":      
        username = username_clean(request, request.POST.get('username'))
        password = clean_password2(request, request.POST.get('password1'), request.POST.get('password2'))
        
        if username is not None and password is not None:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Account has been created successfully')
            return redirect('todolist:login')
    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Wrong username or password!')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title != "" and description != "":
            task = Task(
                title=title,
                description=description,
                user=request.user,
            )
            task.save()
            messages.success(request, "Your task has been saved!")
            return redirect("todolist:show_todolist")

    return render(request, "createtask.html")