from django.urls import path
from . import views

urlpatterns = [
    path('carrera/crear', views.crear_carrera, name='crear_carrera'),
    path('carrera/listar', views.listar_carreras, name='listar_carreras'),
    path('centro/crear', views.crear_centro, name='crear_centro'),
    path('centro/listar', views.listar_centros, name='listar_centro'),
]