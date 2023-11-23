from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('admisiones.urls')),
    path('api/', include('registro.urls')),
    path('api/', include('administrador.urls')),
    path('api/', include('estudiante.urls'))
]


