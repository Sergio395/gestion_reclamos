from django.urls import path
from . import views


urlpatterns = [
    path('nuevo/', views.ReclamoCreateView.as_view(), name='reclamo_form'), # CBV
    path('seguimiento/', views.ReclamoListView.as_view(), name='seguimiento'),
    path('editar/<int:pk>/', views.ReclamoUpdateView.as_view(), name='editar_reclamo'),
    # path('seguimiento/<int:nro_reclamo>/', views.seguimiento_reclamo, name='seguimiento_reclamo')
    # path('nuevo/', views.reclamo_form, name='reclamo_form'), # FVB
    # path('seguimiento/', views.seguimiento, name='seguimiento'),
    # path('api/calles/', views.ObtenerCallesView.as_view(), name='obtener_calles'),
]
