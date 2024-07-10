from django.contrib import admin
from .models import Task, Type, Status

admin.site.register(Task)
admin.site.register(Type)
admin.site.register(Status)
