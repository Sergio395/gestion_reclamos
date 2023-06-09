from django.urls import path
from . import views


urlpatterns = [
    path('', views.admin, name='admin'),
    path('user/', views.UserListView.as_view(), name='usuario'),
    path('nuevo_usuario/', views.UserCreateView.as_view(), name='nuevo_usuario'), 
    path('user/<int:pk>/', views.UserUpdateView.as_view(), name='editar_usuario'),
    path('user/delete/<int:pk>/', views.delete_usuario, name='eliminar_usuario'),
    
    
    path('empresa/', views.ListarEmpresas.as_view(), name='empresa'),
    path('nueva_empresa/', views.nueva_empresa, name='nueva_empresa'),
    path('empresa/<int:id_empresa>/', views.editar_empresa, name='editar_empresa'),
    path('empresa/delete/<int:id_empresa>/', views.delete_empresa, name='eliminar_empresa'),
    
    
    path('orden_compra/', views.OrdencompraListView.as_view(), name='orden_compra'),
    path('nueva_oc/', views.OrdencompraCreateView.as_view(), name='nueva_oc'),
    path('orden_compra/<int:pk>/', views.OrdencompraUpdateView.as_view(), name='editar_oc'),
    path('orden_compra/delete/<int:pk>/', views.delete_oc, name='eliminar_oc'),
    
    
   
]
