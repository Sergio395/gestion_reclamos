from django.urls import path
from .import views


urlpatterns = [
    path('form', views.inspector, name='inicio' ),
    path('nueva', views.carga_inspeccion, name='carga' ),
]
