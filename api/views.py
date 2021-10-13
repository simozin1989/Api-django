import re
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Task
from .serializers import TaskSrializers

# Create your views here.



@api_view(['GET'])
def apiOvervies(request):
    api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
     tasks = Task.objects.all()
     serializers = TaskSrializers(tasks,many=True)
     return Response(serializers.data)



@api_view(['GET'])
def tasDetails(request,pk):
     tasks = Task.objects.get(id=pk)
     serializers = TaskSrializers(tasks,many=False)
     return Response(serializers.data)     



@api_view(['POST'])
def tasCreat(request):
     serializers = TaskSrializers(data=request.data)
     if serializers.is_valid():
         serializers.save
     return Response(serializers.data) 


@api_view(['POST'])
def tasUpate(request,pk):
     tasks = Task.objects.get(id=pk)
     serializers = TaskSrializers( instance=tasks, data=request.data)
     if serializers.is_valid():
         serializers.save()
     return Response(serializers.data)      


@api_view(['DELETE'])
def tasDelet(request,pk):
     tasks = Task.objects.get(id=pk)
     tasks.delete()
     return Response('Item succsesfully delete!') 
