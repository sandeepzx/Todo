from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


# Create your views here.

def home(req):
    task1 = Task.objects.all()
    if req.method == 'POST':
        name = req.POST.get('task','')
        priority = req.POST.get('priority','')
        date = req.POST.get('date','')
        task = Task( name = name, priority = priority, date = date)
        task.save()
    return render(req,"index.html",{'task':task1})

def delete(req,taskid):
    task = Task.objects.get(id = taskid)
    if req.method == 'POST':
        task.delete()
        return redirect('/')
    return render(req,"delete.html")

def update(req,id):
    task = Task.objects.get(id = id)
    f = TodoForm(req.POST or None, instance=task )
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(req,"edit.html", { 'f' : f, 'task' : task })

class TaskListview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task'

class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdatelview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk': self.object.id})
    

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
