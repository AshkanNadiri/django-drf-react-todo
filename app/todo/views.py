from django.shortcuts import render
from .serializer import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserViewSet(viewsets.ModeViewSet):
    """
    API endpoint will let you edit or see the users.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModeViewSet):
    """
    API endpoint will let you edit or see the groups
    """
    queryset = Group.objects.all() 
    serializer_class = GroupSerializer