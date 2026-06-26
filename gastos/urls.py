from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('agregar/', views.agregar_gasto, name = "agregar"),
    path('eliminar/<int:id>/', views.eliminar_gasto, name = "eliminar"),
    path('editar/<int:id>/', views.editar, name = "editar"),
]
