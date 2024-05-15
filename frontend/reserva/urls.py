from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='post_list'),
    path('index', views.index, name='post_list'),
    path('productos', views.productos, name='post_list'),
    path('empleados', views.empleados, name='post_list'),
    path('clientes', views.clientes, name='post_list'),
    path('regiones', views.regiones, name='post_list'),
]