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
    template_name = "detail_task.html"
    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super(). get_context_data()
        context['task'] = self.task
        return context
    # def get_template_names(self):
    #     if self.task.types.exists:

class TaskCreateView(View):
    def dispatch(self, request, *args, **kwargs):
        print(request.POST)
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'add_task.html', {'form': form})
    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
            )
            statuses = form.cleaned_data["statuses"]
            task.statuses.set(statuses)
            types = form.cleaned_data["types"]
            task.types.set(types)
            return redirect('home')
        return render(
            request,
            "add_task.html",
            {"form": form}
        )

class TaskUpdateView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        form = TaskForm(instance=self.task, initial={
            "summary": self.task.summary,
            "description": self.task.description,
            "status": self.task.status,
            "type": self.task.type,
        })
        return render(
            request, "update_task.html",
            context={"form": form}
        )
    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST, instance=self.task)
        if form.is_valid():
            self.task.description = request.POST.get("description")
            self.task.due_date = request.POST.get("due_date")
            self.task.status = request.POST.get("status")
            self.task.save()
            return redirect("task_list")
        else:
            return render(
                request,
                "update_task.html",
                {"form": form})

class TaskDeleteView(TemplateView):
     def post(self, request, *args, **kwargs):
         task = get_object_or_404(Task, pk=self.kwargs['pk'])
         if request.method == 'POST':
             task.delete()
             return redirect('task_list')
         return render(request, 'delete_task.html', {'task': task})