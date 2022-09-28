from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from todolist.form import ToDoForm
from todolist.models import Task

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

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created successfully')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

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
        form = ToDoForm(request.POST)
        if form.is_valid():
            task = Task(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                user=request.user,
            )
            task.save()
            messages.success(request, "Your task has been saved!")
            return redirect("todolist:show_todolist")

    form = ToDoForm()
    context = {"form": form}
    return render(request, "createtask.html", context)