from django.urls import path 
from .views import ListTodoItem, DetailTodoItem

urlpatterns = [
    path('', ListTodoItem.as_view(), name='todo_list'),
    path('<int:pk>/', DetailTodoItem.as_view(), name='todo_detail'),
]
