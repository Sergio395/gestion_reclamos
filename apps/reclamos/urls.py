from django.urls import path
from . import views


urlpatterns = [
    path('nuevo/', views.ReclamoView.as_view(), name='nuevo_reclamo'), # CBV
    path('seguimiento/', views.seguimiento, name='seguimiento'),
    path('seguimiento/<int:nro_reclamo>/', views.seguimiento_reclamo, name='seguimiento_reclamo')
    # path('nuevo/', views.nuevo_reclamo, name='nuevo_reclamo'), # FVB
    # path('api/calles/', views.ObtenerCallesView.as_view(), name='obtener_calles'),
]
