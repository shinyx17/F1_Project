from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='escuderias_inicio'),
    path('listado/', views.listado, name='escuderias_listado'),
]