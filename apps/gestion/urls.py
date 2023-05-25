from django.urls import path
from . import views


urlpatterns = [
    # path('', views.GestionListView.as_view(), name='gestion_index_view'),
    path('', views.gestion_index, name='gestion'),
    path('', views.gestion_index, name='gestion_index'),
    path('nuevo/', views.gestion_nuevo, name='gestion_nuevo'),
    # path('cursos/editar/<int:id_curso>', views.cursos_editar, name='cursos_editar'),
    # path('cursos/eliminar/<int:id_curso>', views.cursos_eliminar, name='cursos_eliminar'),
    # path('', views.gestion_inicio, name='gestion'),
    # path('editar/<int:nro_reclamo>/', views.gestion_editar_reclamo, name='gestion_editar_reclamo'),
]
