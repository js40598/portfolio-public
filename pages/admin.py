from django.contrib import admin
from .models import Page, Skill

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'navbar_display', 'icon')
    list_display_links = ('id', 'title')
    list_editable = ('navbar_display', 'icon')


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level')
    list_display_links = ('id', 'name')
    list_editable = ('level',)


admin.site.register(Page, PageAdmin)
admin.site.register(Skill, SkillAdmin)
