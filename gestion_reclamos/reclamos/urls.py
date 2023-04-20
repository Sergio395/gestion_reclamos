from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('principal/', views.principal, name='principal'),
    path('nr/', views.nuevo_reclamo, name='nuevo-reclamo'),
    path('inspeccion/', views.carga_inspeccion, name='inspeccion'),
    path('certificado/', views.carga_certificado, name='certificado'),
    path('seguimiento/', views.seguimiento, name='seguimiento'),
    path('seguimiento/<int:nro_reclamo>/', views.seguimiento_reclamo, name='seguimiento-reclamo')
]
