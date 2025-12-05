from django.urls import path
from . import views

urlpatterns = [
    # Homepage - shows list of all tasks
    path('', views.task_list, name='task_list'),
    
    # Add new task
    path('add/', views.add_task, name='add_task'),
    
    # Update existing task 
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    
    # Delete task 
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
