from django.urls import path
from gestion import views

urlpatterns = [
    path('gestion', views.gestion_manejo_formulario, name='gestion'),
   
]