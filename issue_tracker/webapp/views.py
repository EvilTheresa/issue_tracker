from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, FormView

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
        context = super().get_context_data()
        context['task'] = self.task
        return context
    # def get_template_names(self):
    #     if self.task.types.exists:


class TaskCreateView(FormView):
    template_name = "add_task.html"
    form_class = TaskForm

    def form_valid(self, form):
        task = form.save()
        return redirect("detail_task", pk=task.pk)


class TaskUpdateView(FormView):
    template_name = "update_task.html"
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
        redirect("detail_task", pk=self.task.pk)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))



class TaskDeleteView(TemplateView):
    template_name = "delete_task.html"
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        if request.method == 'POST':
            task.delete()
            return redirect('task_list')
        return render(request, 'delete_task.html', {'task': task})
