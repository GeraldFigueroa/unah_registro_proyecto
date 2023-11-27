from django.urls import path
from . import views

urlpatterns = [
    path('estudiante/crear', views.crear_estudiante, name='crear_estudiante'),
    path('estudiante/listar', views.listar_estudiantes, name='listar_estudiantes'),
    path('estudiante/login', views.login_estudiante, name='login_estudiante'),
    path('estudiante/perfil/<str:num_cuenta>', views.perfil_estudiante, name='perfil_estudiante'),
    path('tiposolicitud/crear', views.crear_tipoSolicitud, name='crear_tipoSolicitud'),
    path('tiposolicitud/listar', views.listar_tipoSolicitud, name='listar_tipoSolicitud'),
    path('solicitud/crear', views.crear_solicitud, name='crear_solicitud'),
    path('solicitud/listar', views.listar_solicitud, name='listar_solicitud'),
    path('estudiante/password/recuperar/<str:num_cuenta>', views.recuperacion_clave, name='recuperacion_clave'),
    path('estudiante/password/cambiar/', views.cambiar_clave, name='cambiar_clave'),
]