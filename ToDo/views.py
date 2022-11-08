from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ToDoSerializer

from .models import Task
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


#@api_view(['GET', 'POST'])
#def authenticator(request, format=None):
#    content = {
#        'user': str(request.user),
#        'auth': str(request.auth)
#    }
@api_view(['GET'])
def overview(request):
    api_overview = {
        'api': '/api'
    }
    return Response(api_overview)


@api_view(['GET'])
def task_list(request):
    queryset = Task.objects.all()
    serializer = ToDoSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = ToDoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    serializer = ToDoSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request, pk):
    item = Task.objects.get(id=pk)
    item.delete()
    return Response('Item Successfully Removed')
