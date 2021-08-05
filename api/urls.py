from django.urls import path
from .views import *

urlpatterns = [
    path('', tasklist, name = "tasklist"),
    path('task_detail/<str:pk>/', taskDetail, name='taskdetail'),
    path('task_create/', taskCreate, name='taskcreate'),
    path('task_update/<str:pk>/', taskUpdate, name='taskupdate'),
    path('task_delete/<str:pk>/', taskDelete, name='taskdelete'),
]
