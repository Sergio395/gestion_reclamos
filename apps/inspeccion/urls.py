from django.urls import path
from . import views
from apps.inspeccion.views import InspeccionListView
from .views import *

urlpatterns = [

 
    path('', views.inspeccion, name='index_inspeccion' ),
    path('inspeccion', views.InspeccionListView.as_view(), name='inspeccion' ),
    path('carga_inspeccion', views.InspeccionesCreateView.as_view(), name='carga_inspeccion' ),
    path('editar_inspeccion/<int:pk>/', views.InspeccionesUpdateView.as_view(), name='editar_inspeccion' ),
    path('eliminar_inspeccion/<int:pk>/', views.delete_inspeccion, name='eliminar_inspeccion'),  
    #path('grabar_inspeccion/<int:pk>/', views.grabar_numero, name='grabar_inspeccion'), 

    path('ver_reclamo/<int:pk>/', views.mostrar_reclamo, name='mostrar_reclamo'),
    
    
    
       

]
