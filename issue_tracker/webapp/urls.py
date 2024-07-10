from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('add/', views.TaskCreateView.as_view(), name='add_task'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='detail_task'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete_task'),
]

