from django.urls import path
from . import views

urlpatterns = [
    path('admision/crear', views.crear_admision, name='crear_admision'),
    path('admision/listar', views.obtener_admisiones, name='obtener_admisiones'),
    path('requerimiento/crear', views.crear_requerimiento, name='crear_requerimiento'),
    path('requerimiento/listar', views.obtener_requerimiento, name='obtener_requerimiento'),
    path('calificacion/crear', views.crear_calificacion, name='crear_calificacion'),
    path('calificacion/listar', views.obtener_calificaciones, name='obtener_calificaciones'),
    path('calificacion/enviar', views.enviar_calificaciones, name='enviar_calificaciones'),
    path('admision/resultados/<str:id>', views.obtener_resultados, name='obtener_resultados'),
]
