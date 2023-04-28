from django.urls import path
from . import views


urlpatterns = [
    path('', views.admin, name='admin'),
    path('user', views.usuario, name='usuario')
]
