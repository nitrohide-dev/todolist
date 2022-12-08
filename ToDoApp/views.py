from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    return render(request,'index.html', {'task':Task.objects})
def enqueue(request):
    all_tasks = Task.objects
    print("nigger!")
    if request.method == "POST":
        print("nigger3!")
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        return redirect('index')

def dequeue(request):
    print("nigger2!")
    if(Task.objects.exists()):
        task_id2 = Task.objects.first().id
        task = Task.objects.get(id=task_id2)
        task.delete()
        return redirect('index')
    return redirect('index')

