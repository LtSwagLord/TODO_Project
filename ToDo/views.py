from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ToDoSerializer

from .models import ToDo
# Create your views here.


@api_view(['GET'])
def task_list(request):
    tasks = ToDo.objects.all()
    serializer = ToDoSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = ToDoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def task_update(request, pk):
    task = ToDo.objects.get(id=pk)
    serializer = ToDoSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request, pk):
    item = ToDo.objects.get(id=pk)
    item.delete()
    return Response('Item Successfully Removed')
