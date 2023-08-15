from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # URL para listar laboratorios

    path('listar/', views.listar_laboratorios, name='listar_laboratorios'),

    # URL para crear un nuevo laboratorio
    path('crear/', views.crear_laboratorio, name='crear_laboratorio'),

    # URL para ver detalles de un laboratorio específico (reemplaza '<int:laboratorio_id>' con el ID del laboratorio)
    path('<int:laboratorio_id>/', views.detalle_laboratorio, name='detalle_laboratorio'),

    # URL para actualizar un laboratorio existente (reemplaza '<int:laboratorio_id>' con el ID del laboratorio)
    path('<int:laboratorio_id>/actualizar/', views.actualizar_laboratorio, name='actualizar_laboratorio'),

    # URL para eliminar un laboratorio existente (reemplaza '<int:laboratorio_id>' con el ID del laboratorio)
    path('<int:laboratorio_id>/eliminar/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
]
