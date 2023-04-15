from django.urls import path
from . import views



urlpatterns = [
    
    path('index/', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('principal/', views.principal, name='principal'),
    path('comenzar/', views.carga_reclamo, name='reclamos'),
    path('inspeccion/', views.carga_inspeccion, name='inspeccion'),
    path('certificado/', views.carga_certificado, name='certificado'),
]