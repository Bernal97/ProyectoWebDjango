from django.http import request
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import CategoriaForm, RegistroForm, ProductoForm, ContactoForm
from .models import Producto
from .carrito import Carrito
from django.db.models import Q

# Create your views here.

def principal(request):
    products = Producto.objects.all()
    busqueda = request.GET.get("Buscar")

    if busqueda:
        products = Producto.objects.filter(
            Q(nombre__icontains = busqueda) 
        ).distinct
    return render(request, "JugueteriaApp/inicio.html",{"products": products})


def Categoria (request):
    return render(request, "JugueteriaApp/categoria.html")

def acercaDe(request):
    return render(request, "JugueteriaApp/acercaDe.html")

def carritoCompras(request):
    return render(request, "JugueteriaApp/carrito.html")

def Contacto (request):
   formulario_contacto = ContactoForm()
   return render(request, "JugueteriaApp/contacto.html",{'miFormulario': formulario_contacto})
   

def registro(request):
    data = {
        'form': RegistroForm()
    }
    if request.method == 'POST':
        formulario = RegistroForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            return redirect(to="Principal")
        data["form"] = formulario
    return render(request,"registration/registro.html", data)

def carrito(request):
    return render(request, "JugueteriaApp/carrito.html")

def agregarproducto(request):

    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="Principal")
        data["form"] = formulario
    return render(request, "productos/agregar.html", data)

def modificarproducto(request, id):
    producto = Producto.objects.get(id = id)
    data = {
        'form': ProductoForm (instance= producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data = request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return redirect(to = "Principal")
        data["form"] = formulario
    return render(request, 'productos/modificar.html', data)

def eliminarproducto(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect(to = "Principal")

def AñadirProductoCarro (request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = id)

    carrito.añadir(PRODUCTO = producto)
    return redirect(to = "CarritoCompras")

def EliminarProductoCarro (request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)

    carrito.remove(producto = producto)

    return redirect("Carro")

def RestarProductoCarro (request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = id)

    carrito.decrementar(PRODUCTO = producto)
    return redirect(to = "CarritoCompras")

def LimpiarProductoCarro(request):
    carrito = Carrito(request)
    carrito.clear()
    return redirect (to = "CarritoCompras")