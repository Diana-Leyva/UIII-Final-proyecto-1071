from django.urls import path
from empleado_app import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarEmpleado/", views.registrarEmpleado, name="registrarEmpleado"),
    path("borrarEmpleado/<idempleado>", views.borrarEmpleado, name="borrarEmpleado"),
    path("seleccionarEmpleado/<idempleado>", views.seleccionarEmpleado, name="seleccionarEmpleado"),
    path("editarEmpleado/", views.editarEmpleado, name="editarEmpleado"),
    path("gestionarEmpleado/", views.inicio_vista, name="gestionarEmpleado")
]
