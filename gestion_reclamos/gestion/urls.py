from django.urls import path
from gestion import views



urlpatterns = [
    path('', views.gestion_ver_reclamos, name='gestion'),
    path('/editar', views.gestion_editar_reclamo, name='gestion_editar_reclamo'),
]
