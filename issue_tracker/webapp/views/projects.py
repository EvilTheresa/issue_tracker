from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ..forms import SearchForm, ProjectForm
from ..models import Task
from ..models.projects import Project


class ProjectListView(ListView):
    model = Project
    template_name = "projects/index.html"
    context_object_name = "projects"
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        form = self.form
        if form.is_valid():
            return form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(name__contains=self.search_value) | Q(description__contains=self.search_value)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form
        if self.search_value:
            context["search"] = urlencode({"search": self.search_value})
            context["search_value"] = self.search_value
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(project=self.object)
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/project_add.html"
    success_url = reverse_lazy('project_list')


class ProjectUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/project_update.html"
    success_url = reverse_lazy('project_list')
    permission_required = "webapp.change_project"

    def has_permission(self):
        # return self.request.user.groups.filter(name="moderators").exists()
        return super().has_permission() or self.request.user == self.get_object().user


class ProjectDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')
    template_name = "projects/project_confirm_delete.html"
    permission_required = "webapp.delete_project"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().user