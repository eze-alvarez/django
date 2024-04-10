from django.urls import path
from . import views 

urlpatterns = [
    path('listar-productos/', views.listar_productos, name='listar_productos'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar-proveedor/', views.agregar_proveedor, name='agregar_proveedor')
]
