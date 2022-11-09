from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import ToDoSerializer
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token

from .models import Task
from rest_framework import permissions
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
# Create your views here.


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def post(self, serializer):
        if serializer.is_valid():
            serializer.save(owner=self.request.user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]



