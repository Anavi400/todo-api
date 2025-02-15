from django.shortcuts import render
from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework import generics


# Create your views here.

class ListTodoItem(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class DetailTodoItem(generics.RetrieveAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    
