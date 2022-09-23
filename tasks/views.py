
from multiprocessing import context
from . forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here


def index(request):
    tasks = MyTask.objects.all()

    form = TaskForm()

    if request.method == 'POST':

        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):
    task = MyTask.objects.get(id=pk)

    form=TaskForm(instance=task)
    context={'form':form}

    if request.method == 'POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

        
        return render (request,'tasks/update_task.html',context)
    return render (request,'tasks/update_task.html',context)
def deleteTask(request,pk):
    item=MyTask.objects.get(id=pk)
    if request.method =='POST':
        item.delete()
        return redirect('/')


    context= {'item':item}
    return render(request,'tasks/delete.html',context)