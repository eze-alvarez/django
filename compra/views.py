from django.shortcuts import render,redirect
from .models import Producto, Proveedor
from django.http import HttpResponse 
from django.template import Template, Context

# Create your views here.


def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'compra/listar_productos.html', {'productos': productos})


def agregar_producto(request):
    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock_actual = request.POST.get('stock_actual')
        proveedor_id = request.POST.get('proveedor')

        Producto.objects.create(nombre=nombre, precio=precio, stock_actual=stock_actual, proveedor_id=proveedor_id)
        return redirect('listar_productos')
    else:
        proveedores = Proveedor.objects.all()
        return render(request, 'compra/agregar_producto.html', {'proveedores': proveedores})



def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')

        Proveedor.objects.create(nombre=nombre, apellido=apellido, dni=dni)
        return redirect('listar_productos')
    else:
        return render(request, 'compra/agregar_proveedor.html')