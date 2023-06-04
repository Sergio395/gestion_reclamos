from django.urls import path
from . import views


urlpatterns = [
    path('', views.gestion_index, name='gestion'),
    path('', views.gestion_index, name='gestion_index'),

    path('nuevo/', views.gestion_nuevo, name='gestion_nuevo'),
    path('buscar/', views.gestion_buscar, name='gestion_buscar'),
    path('editar/<int:id>', views.gestion_editar, name='gestion_editar'),
    path('eliminar/<int:id>', views.gestion_eliminar, name='gestion_eliminar'),
    
    path('lista/', views.GestionListView.as_view(), name='gestion_lista'),
    
    # path('', views.gestion_inicio, name='gestion'),
    # path('editar/<int:nro_reclamo>/', views.gestion_editar_reclamo, name='gestion_editar_reclamo'),
]
