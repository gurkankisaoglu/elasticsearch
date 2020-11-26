from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Task admin."""

    list_display = ('name',)
    search_fields = ('name',)

@admin.register(TaskUser)
class AuthorAdmin(admin.ModelAdmin):
    """Task user admin."""

    list_display = ('name',)
    search_fields = ('name',)
