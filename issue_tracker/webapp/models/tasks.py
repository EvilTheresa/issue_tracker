from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from .projects import Project
from .statuses import Status
from .types import Type


class Task(models.Model):
    summary = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ManyToManyField(
        Type,
        related_name="tasks",
        verbose_name="Типы",
        blank=True,
        through='TaskType',
        through_fields=("task", "type"),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        get_user_model(),
        related_name="tasks",
        on_delete=models.SET_DEFAULT,
        default=1
    )

    def __str__(self):
        return self.summary

    def get_absolute_url(self):
        return reverse("webapp:task_detail", kwargs={"pk": self.pk})
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class TaskType(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)