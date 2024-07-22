from django.contrib import admin
from .models import Task, Type, Status
from .models.projects import Project

admin.site.register(Task)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project)