from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from .views.projects import ProjectListView, ProjectDetailView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('add/', TaskCreateView.as_view(), name='add_task'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='detail_task'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),

    path('project/', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]

