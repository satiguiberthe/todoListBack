# tasks/views.py
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer


class ListTodo(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CreateTodo(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DeleteTodo(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


