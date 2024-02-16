from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('torta/', views.jamon,name='torta'),
    path('hello/<str:username>', views.hello,name='hello'),
    path('project/', views.Project,name='projects'),
    path('project/<int:id>', views.project_details,name='details'),
    path('tasks/', views.Tasks,name='tasks'),
    path('create_task/',views.create_Task,name='create_task'),
    path('create_project/',views.create_Project,name='create_project')
]
