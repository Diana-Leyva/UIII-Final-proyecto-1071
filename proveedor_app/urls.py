from django.urls import path
from proveedor_app import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarProveedor/", views.registrarProveedor, name="registrarProveedor"),
    path("borrarProveedor/<idproveedor>", views.borrarProveedor, name="borrarProveedor"),
    path("editarProveedor/<idproveedor>", views.editarProveedor, name="editarProveedor"),
    path("seleccionarProveedor/<idproveedor>", views.seleccionarProveedor, name="seleccionarProveedor"),
    path("gestionarProveedor/",views.inicio_vista, name="gestionarProveedor")
]
