from django.urls import path
from . import views


urlpatterns = [
    path('', views.gestion_index, name='gestion'),
    path('', views.gestion_index, name='gestion_index'),

    path('nuevo/', views.gestion_nuevo, name='gestion_nuevo'),
    path('buscar/', views.gestion_buscar, name='gestion_buscar'),
    path('editar/<int:id>', views.gestion_editar, name='gestion_editar'),
    path('eliminar/<int:id>', views.gestion_eliminar, name='gestion_eliminar'),
    
    # -- VBC --
    path('lista/', views.GestionListView.as_view(), name='gestion_lista'),
    path('nuevo/<int:pk>/', views.GestionCreateView.as_view(), name='gestion_nuevo'),
    path('editar/<int:pk>/', views.GestionUpdateView.as_view(), name='gestion_form'),
    
    # path('nuevo/', views.ReclamoCreateView.as_view(), name='reclamo_form'),
    # path('seguimiento/', views.ReclamoListView.as_view(), name='seguimiento'),
    # path('editar/<int:pk>/', views.ReclamoUpdateView.as_view(), name='editar_reclamo'),
    # path('borrar/<int:id_reclamo>/', views.reclamo_delete, name='borrar_reclamo'),
]
