

from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [

     path('', views.apiOvervies, name='api-overview'),
     path('task-list/', views.tasklist, name='task-lis'),
     path('task-detail/<str:pk>/', views.tasDetails, name='task-detail'),
     path('task-create/', views.tasCreat, name='task-create'),
     path('task-update/<str:pk>/', views.tasUpate, name='task-update'), 
     path('task-delete/<str:pk>/', views.tasDelet, name='task-delete'),
]
