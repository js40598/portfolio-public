from django.contrib import admin
from .models import Project, Subpage

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'init_date', 'planned_finish_date')
    list_display_links = ('id', 'title')
    list_per_page = 25


class SubpageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'project', 'icon')
    list_display_links = ('id', 'title')
    list_per_page = 25


admin.site.register(Project, ProjectAdmin)
admin.site.register(Subpage, SubpageAdmin)
