from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'task_name', 'description', 'created', 'status', 'owner']


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks']
