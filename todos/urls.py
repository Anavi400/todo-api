from django.urls import path 
from .views import ListTodoItem

urlpatterns = [
    path('', ListTodoItem.as_view(), name='todo_list'),
]
