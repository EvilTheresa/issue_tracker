from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from .models import Task
from .forms import TaskForm

class TaskListView(TemplateView):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'home.html', {'tasks': tasks})
class TaskDetailView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super(). get_context_data()
        context['tasks'] = self.task
        return context
    # def get_template_names(self):
    #     if self.task.types.exists:

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


def update_task(request, *args, pk, **kwargs):
    if request.method == "GET":
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(initial={
            "description": task.description,
            "due_date": task.due_date,
            "status": task.status,
        })
        return render(
            request, "update_task.html",
            context={"form": form}
        )
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = get_object_or_404(Task, pk=pk)
            task.description = request.POST.get("description")
            task.due_date = request.POST.get("due_date")
            task.status = request.POST.get("status")
            task.save()
            return redirect("task_list")
        else:
            return render(
                request,
                "update_task.html",
                {"form": form}
            )
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})