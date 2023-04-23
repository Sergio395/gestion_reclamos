from django.urls import path, include
from gestion import views

urlpatterns = [
    path('gestion', include('gestion.urls'), views.gestion_manejo_formulario, name='gestion_manejo_formulario'),
   
]