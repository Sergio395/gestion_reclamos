from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('principal/', views.principal, name='principal'),
    path('comenzar/', views.carga_reclamo, name='reclamos'),
    path('inspeccion/', views.carga_inspeccion, name='inspeccion'),
    path('certificado/', views.carga_certificado, name='certificado'),
]