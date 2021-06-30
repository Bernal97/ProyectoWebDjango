from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', views.principal, name = "Principal"),
    path('acercaDe', views.acercaDe, name = "AcercaDe"),
    path('categoria', views.Categoria, name = "categoria"),
    path('registro', views.registro, name = "Registro"),
    path('contacto', views.Contacto, name = "Contacto"),
    path('carritoCompras', views.carritoCompras, name = "CarritoCompras"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('agregarproducto', views.agregarproducto, name = "agregarproducto"),
    path('login/', LoginView.as_view(template_name= 'registration/login.html'), name = 'Login'),
    path('modificarproducto/<id>/', views.modificarproducto, name = "modificarproducto"),
    path('eliminarproducto/<id>/', views.eliminarproducto, name = "eliminarproducto"),
    path('agregarCarrito/<id>/', views.AñadirProductoCarro, name = "agregarProductoCarro"),
    path('eliminarCarrito/<id>/', views.EliminarProductoCarro, name = "eliminarProductoCarro"),
    path('restarCarrito/<id>/', views.RestarProductoCarro, name = "restarProductoCarro"),
    path('limpiarCarrito', views.LimpiarProductoCarro, name = "limpiarProductoCarro"),

]
