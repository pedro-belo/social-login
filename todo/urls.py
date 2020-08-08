from django.urls import path
from todo import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo, name='todo'),
    path('add/', views.addTodo, name='add'),
    path('stage/<int:task_id>/<int:new_stage>/',
         views.change_stage, name='stage'),
    path('stage/<int:task_id>/', views.delete_task, name='delete')
]
