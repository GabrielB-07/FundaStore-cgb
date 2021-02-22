from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import FormularioProducto

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'nosotros.html')

@login_required
def listarProductos(request):
    productos =Producto.objects.all()
    contexto = {'productos':productos}
    return render(request, 'ListarProductos.html',context=contexto)

@login_required   
def agregarProductos(request):
    request.accion = 'C'
    if request.method == 'POST':
        formulario = FormularioProducto(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarProductos')
    else:
        formulario = FormularioProducto()
    contexto = {'formulario':formulario}
    return render(request, 'AgregarProductos.html',context=contexto)

@login_required
def editarProducto(request, id):
    request.accion = 'U'
    producto = Producto.objects.get(pro_id = id)
    if request.method == 'POST':
        formulario = FormularioProducto(request.POST,request.FILE, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarProductos')
    else:
        formulario = FormularioProducto(instance=producto)
    contexto = {'formulario':formulario}
    return render(request, 'AgregarProductos.html',context=contexto)

@login_required
def eliminarProducto(request, id):
    request.accion = 'D'
    producto = Producto.objects.get(pro_id = id)
    producto.delete()
    return redirect('listarProductos')