from django.urls import path
from .views import task_list, create_task, create_category, delete_task, complete_task

app_name = 'tasks'

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', create_task, name='create_task'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('create_category/', create_category, name='create_category')
]
