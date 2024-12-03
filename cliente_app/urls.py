from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarCliente/", views.registrarCliente, name="registrarCliente"),
    path("borrarCliente/<codigo>", views.borrarCliente, name="borrarCliente"),
    path("seleccionarCliente/<codigo>", views.seleccionarCliente, name="seleccionarCliente"),
    path("editarCliente/", views.editarCliente, name="editarCliente"),
    path("gestionarCliente/", views.inicio_vista, name="gestionarCliente"),  # Aquí agregamos la URL para gestionarCliente
]