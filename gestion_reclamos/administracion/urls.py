from django.urls import path
from . import views


urlpatterns = [
    path('', views.admin, name='admin'),
    path('user', views.usuario, name='usuario'),
    path('user/<int:usuario_num>/', views.edit_usuario, name='editar_usuario'),
    path('delete/<int:usuario_num>/', views.delete_usuario, name='eliminar_usuario'),
    path('empresa', views.empresa, name='empresa'),
    path('nueva_empresa', views.nueva_empresa, name='nueva_empresa'),
    path('nuevo_usuario', views.nuevo_usuario, name='nuevo_usuario')
]
