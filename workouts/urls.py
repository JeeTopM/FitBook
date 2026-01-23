from django.urls import path
from . import views

app_name = 'workouts'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_exercise, name='add_exercise'),
    path('list/', views.exercise_list, name='exercise_list'),
    path('delete/<int:exercise_id>/', views.delete_exercise, name='delete_exercise'),
]