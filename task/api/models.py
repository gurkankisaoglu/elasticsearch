from django.db import models
from django.conf import settings

class TaskUser(models.Model):
    """Task."""

    name = models.CharField(max_length=200)

    class Meta(object):
        """Meta options."""
        ordering = ["id"]

    def __str__(self):
        return self.name


class Task(models.Model):
    """Task"""

    name = models.CharField(max_length=30)
    created_by = models.ForeignKey(TaskUser, on_delete='CASCADE')

    class Meta(object):
        """Meta options."""
        ordering = ["id"]

    def __str__(self):
        return self.name
