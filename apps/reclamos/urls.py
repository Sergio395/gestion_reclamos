from django.urls import path
from . import views


urlpatterns = [
    # path('nuevo/', views.NuevoReclamoView, name='nuevo_reclamo'), # CBV
    path('nuevo/', views.nuevo_reclamo, name='nuevo_reclamo'), # FVB
    path('seguimiento/', views.seguimiento, name='seguimiento'),
    path('seguimiento/<int:nro_reclamo>/', views.seguimiento_reclamo, name='seguimiento-reclamo')
]
