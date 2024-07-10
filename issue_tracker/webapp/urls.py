from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='detail_task'),
    path('task/<int:pk>/update/', views.update_task, name='update_task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
]

