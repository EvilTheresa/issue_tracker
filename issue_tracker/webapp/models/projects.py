from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from accounts.views import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(
        get_user_model(),
        related_name="projects",
        on_delete=models.SET_DEFAULT,
        default=1
    )

    def get_absolute_url(self):
        return reverse('webapp:project-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
