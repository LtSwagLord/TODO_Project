from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.models):
    class Meta:
        model = ToDo
        fields = "__all__"
