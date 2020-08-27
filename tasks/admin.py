from django.contrib import admin
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_done', 'priority', 'project')
    list_display_links = ('id', 'title')
    list_filter = ('project', 'priority')
    list_editable = ('is_done', 'priority')
    list_per_page = 25


admin.site.register(Task, TaskAdmin)
