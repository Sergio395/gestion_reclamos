from django.urls import path
from . import views


urlpatterns = [
    path('', views.inspeccion, name='inspeccion' ),
    path('carga-inspeccion', views.carga_inspeccion, name='carga_inspeccion' ),
    path('carga-certificacion', views.carga_certificacion, name='carga_certificacion' ),
]
