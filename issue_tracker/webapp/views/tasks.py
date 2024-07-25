from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView,  ListView, CreateView, DeleteView, UpdateView

from ..models import Task, Project
from ..forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/home.html'


class TaskDetailView(TemplateView):
    template_name = "tasks/detail_task.html"

    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['task'] = self.task
        return context


class TaskCreateView(CreateView):
    template_name = "tasks/add_task.html"
    form_class = TaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect("webapp:project_detail", pk=self.kwargs['pk'])


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/update_task.html"
    context_object_name = 'task'

    def get_success_url(self):
        return reverse_lazy('webapp:project_detail', kwargs={'pk': self.object.project.pk})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"
    context_object_name = 'task'

    def get_success_url(self):
        return reverse_lazy('webapp:project_detail', kwargs={'pk': self.object.project.pk})
