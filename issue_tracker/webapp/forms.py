from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'status': forms.Select(),
            'type': forms.CheckboxSelectMultiple(),
        }
