from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import *

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login as login, logout

from . filter import *

# Create your views here.
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print('username or password is wrong')    

    
    context = {}
    return render(request, 'tasks/login.html', context)

def register(request):
    regform = CreateUserForm()
    if request.method == 'POST':
        regform = CreateUserForm(request.POST)
        if regform.is_valid():
            regform.save()
            return redirect('login')

    context = {'regform':regform}
    return render(request, 'tasks/register.html', context)

def logoutpage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  

    myFilter = todoFilter(request.GET, queryset=tasks) #filtering for search
    tasks = myFilter.qs         

    context = {'tasks':tasks, 'form':form, 'myFilter':myFilter}
    return render(request, 'tasks/list.html', context)

@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')


    context = {'form':form}
    return render(request, 'tasks/update_task.html', context)   

@login_required(login_url='login')
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('index')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context) 


