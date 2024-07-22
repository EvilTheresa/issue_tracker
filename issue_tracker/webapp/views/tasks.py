from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, FormView, ListView

from ..models import Task
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


class TaskCreateView(FormView):
    template_name = "tasks/add_task.html"
    form_class = TaskForm

    def form_valid(self, form):
        task = form.save()
        return redirect("detail_task", pk=task.pk)


class TaskUpdateView(FormView):
    template_name = "tasks/update_task.html"
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs.get("pk"))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def form_valid(self, form):
        form.save()
        return redirect("detail_task", pk=self.task.pk)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class TaskDeleteView(TemplateView):
    template_name = "tasks/delete_task.html"

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        if request.method == 'POST':
            task.delete()
            return redirect('task_list')
        return render(request, 'tasks/delete_task.html', {'task': task})
