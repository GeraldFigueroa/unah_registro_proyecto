from django.urls import path
from . import views

urlpatterns = [
    path('estudiante/crear', views.crear_estudiante, name='crear_estudiante'),
    path('estudiante/listar', views.listar_estudiantes, name='listar_estudiantes'),
    path('estudiante/login', views.login_estudiante, name='login_estudiante'),
]