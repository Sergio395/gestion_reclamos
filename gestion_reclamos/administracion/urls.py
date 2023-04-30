from django.urls import path
from . import views


urlpatterns = [
    path('', views.admin, name='admin'),
    path('user', views.usuario, name='usuario'),
    path('empresa', views.empresa, name='empresa'),
    path('nueva_empresa', views.nueva_empresa, name='nueva_empresa'),
    path('nuevo_usuario', views.nuevo_usuario, name='nuevo_usuario')
]
