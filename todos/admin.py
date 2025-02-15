from django.contrib import admin
from .models import TodoItem
# Register your models here.


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'completed', 'created', 'updated']
    list_filter = ['completed', 'created']
    search_fields = ['title'] 

admin.site.register(TodoItem, TodoItemAdmin)

