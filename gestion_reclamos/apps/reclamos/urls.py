from django.urls import path
from . import views


urlpatterns = [
    path('nuevo/', views.nuevo_reclamo, name='nuevo_reclamo'),   
    path('seguimiento/', views.seguimiento, name='seguimiento'),
    path('seguimiento/<int:nro_reclamo>/', views.seguimiento_reclamo, name='seguimiento-reclamo')
]
