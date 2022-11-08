from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='api-overview'),
    path('task-list/', views.task_list, name='task-list'),
    path('task-add/', views.task_create, name='task-add'),
]