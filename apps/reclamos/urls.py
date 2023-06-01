from django.urls import path
from . import views


urlpatterns = [
    path('nuevo/', views.ReclamoCreateView.as_view(), name='reclamo_form'),
    path('seguimiento/', views.ReclamoListView.as_view(), name='seguimiento'),
    path('editar/<int:pk>/', views.ReclamoUpdateView.as_view(), name='editar_reclamo'),
    path('borrar/<int:id_reclamo>/', views.reclamo_delete, name='borrar_reclamo'),
    # path('api/calles/', views.ObtenerCallesView.as_view(), name='obtener_calles'),
]
