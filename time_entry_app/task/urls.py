from django.urls import path
from task import views

urlpatterns = [
    path('', views.task_home),
    path('add/', views.add_task),
    path('track/', views.task_task),
    path('list/', views.task_list),
]
