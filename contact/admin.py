from django.contrib import admin
from .models import Message

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'email', 'is_answered')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'company', 'email')
    list_per_page = 25
    list_editable = ('is_answered', )
    list_filter = ('email',)


admin.site.register(Message, MessageAdmin)
