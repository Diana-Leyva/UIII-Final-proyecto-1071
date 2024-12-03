from django.urls import path
from sucursal_app import views

urlpatterns = [
    path("sucursal", views.inicio_vista, name="sucursal"),
    path("registrarSucursal/", views.registrarSucursal, name="registrarSucursal"),
    path("borrarSucursal/<int:codigo>", views.borrarSucursal, name="borrarSucursal"),
    path("editarSucursal/<int:codigo>", views.editarSucursal, name="editarSucursal"),
    path("seleccionarSucursal/<int:codigo>", views.seleccionarSucursal, name="seleccionarSucursal"),
    path("gestionarSucursal/", views.inicio_vista, name="gestionarSucursal")
]
