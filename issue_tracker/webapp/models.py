from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Statuses'

class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.summary

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

class TaskType(models.Model):
    task = models.ForeignKey('Task', related_name='types_tasks', on_delete=models.CASCADE, )
    type = models.ForeignKey('Type', related_name='tasks_types', on_delete=models.CASCADE, )
