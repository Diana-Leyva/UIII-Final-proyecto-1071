from django.urls import path
from empleado_app import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarEmpleado/", views.registrarEmpleado, name="registrarEmpleado"),
    path("borrarEmpleado/<codigo>", views.borrarEmpleado, name="borrarEmpleado"),
    path("seleccionarEmpleado/<codigo>", views.seleccionarEmpleado, name="seleccionarEmpleado"),
    path("editarEmpleado/", views.editarEmpleado, name="editarEmpleado"),
    path("gestionarEmpleado/", views.inicio_vista, name="gestionarEmpleado")
]
