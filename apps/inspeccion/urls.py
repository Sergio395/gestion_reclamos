from django.urls import path
from . import views
from apps.inspeccion.views import InspeccionListView
from .views import *

urlpatterns = [
    path('', views.inspeccion, name='index_inspeccion' ),
    path('inspeccion/', views.inspeccion, name='inspeccion' ),
    path('listar_inspeccion', views.InspeccionListView.as_view(), name='inspecciones' ),
    path('carga_inspeccion/', views.InspeccionesCreateView.as_view(), name='carga_inspeccion' ),
    path('editar_inspeccion/<int:pk>/', views.InspeccionesUpdateView.as_view(), name='editar_inspeccion' ),
    path('eliminar_inspeccion/<int:pk>//', views.delete_inspeccion, name='eliminar_inspeccion'),  
    path('ver_reclamo/<int:pk>/', views.mostrar_reclamo, name='mostrar_reclamo'),
    
    
    path('inspeccion-form/', inspeccion_form, name='inspeccion_form')
    
       

]
