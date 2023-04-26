from django.urls import path
from gestion import views


urlpatterns = [
    path('', views.gestion_manejo_formulario, name='gestion'),
]
