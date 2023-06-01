from django.urls import path
from . import views
from apps.inspeccion.views import InspeccionListView
from .views import *

urlpatterns = [

 
    path('', views.inspeccion, name='inspeccion' ),
    # path('carga-inspeccion', views.carga_inspeccion, name='carga_inspeccion' ),
    path('carga-certificacion', views.carga_certificacion, name='carga_certificacion' ),
    # path('db_inspeccion', views.db_inspeccion, name='db_inspeccion' ),
    
   

]
