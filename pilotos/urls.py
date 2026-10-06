from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='pilotos_inicio'),
    path('listado/', views.listado, name='pilotos_listado'),
]