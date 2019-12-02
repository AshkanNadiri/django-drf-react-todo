from django.shortcuts import render
from .serializer import UserSerializer, GroupSerializer, TodoSerializer
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Todo

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint will let you edit or see the users.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint will let you edit or see the groups
    """
    queryset = Group.objects.all() 
    serializer_class = GroupSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer