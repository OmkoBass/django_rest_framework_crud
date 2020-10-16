from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiMain, name='api-main'),
    path('all/', views.todoAll, name='todo-all'),
    path('todo/<str:pk>', views.todoById, name='todo-by-id'),
    path('todo-create/', views.todoCreate, name='todo-create'),
    path('todo-update/<str:pk>/', views.todoUpdate, name='todo-update'),
    path('todo-delete/<str:pk>/', views.todoDelete, name='todo-delete'),
]
