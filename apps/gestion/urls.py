from django.urls import path
from . import views


urlpatterns = [
    # path('', views.gestion_index, name='gestion'),
    # path('', views.gestion_index, name='gestion_index'),

    # -- FBV --
    path('nuevo/', views.gestion_nuevo, name='gestion_nuevo'),
    path('buscar/', views.gestion_buscar, name='gestion_buscar'),
    path('editar/<int:id>', views.gestion_editar, name='gestion_editar'),
    path('eliminar/<int:id>', views.gestion_eliminar, name='gestion_eliminar'),
    
    # -- CBV --
    path('', views.GestionListView.as_view(), name='gestion'),
    path('cbvlista/', views.GestionListView.as_view(), name='gestioncbv_lista'),
    path('cbvinspeccionlista/', views.InspeccionListView.as_view(), name='inspeccioncbv_lista'),
    path('cbvnuevo/', views.GestionCreateView.as_view(), name='gestioncbv_nuevo'),
    path('cbvdetalle/<int:pk>/', views.GestionDetailView.as_view(), name='gestioncbv_detalle'),
    path('cbveditar/<int:pk>/', views.GestionSoloUpdateView.as_view(), name='gestioncbv_editar'),
    # path('cbvcompletoeditar/<int:pk>/', views.GestionCompletoUpdateView.as_view(), name='gestioncompletocbv_editar'),
    path('cbvborrar/<int:pk>/', views.GestionDeleteView.as_view(), name='gestioncbv_borrar'),
    
]
