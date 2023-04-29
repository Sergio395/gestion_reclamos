from django.urls import path
from gestion import views



urlpatterns = [
    path('', views.gestion_inicio, name='gestion'),
    path('editar', views.gestion_editar_reclamo, name='gestion_editar_reclamo'),
    path('editar/<int:nro_reclamo>/', views.gestion_editar_reclamo, name='gestion_editar_reclamo')
]
