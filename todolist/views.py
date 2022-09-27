from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from todolist.form import ToDoForm
from todolist.models import Task

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user).all()
    context = {
    'list_task': data_task,
    }
    return render(request, "todolist.html", context)

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