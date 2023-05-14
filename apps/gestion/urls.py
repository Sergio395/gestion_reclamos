from django.urls import path
from . import views


urlpatterns = [
    path('', views.gestion_inicio, name='gestion'),
    path('editar/<int:nro_reclamo>/', views.gestion_editar_reclamo, name='gestion_editar_reclamo'),
]
