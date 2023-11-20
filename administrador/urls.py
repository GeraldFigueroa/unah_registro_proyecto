from django.urls import path
from . import views

urlpatterns = [
    path('empleado/crear', views.crear_empleado, name='crear_empleado'),
    path('empleado/listar', views.obtener_empleados, name='obtener_empleados'),
    path('usuario/crear', views.crear_usuario, name='crear_usuario'),
    path('usuario/listar', views.obtener_usuarios, name='obtener_usuarios'),
    
]