from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarOrden/", views.registrarOrden, name='registrarOrden'),  # Ruta para registrar una nueva orden
    path("editarOrden/", views.editarOrden, name='editarOrden'),  # Ruta para editar una orden existente
    path("seleccionarOrden/<codigo>", views.seleccionarOrden, name="seleccionarOrden"),
    path("borrarOrden/<codigo>", views.borrarOrden, name='borrarOrden'),  # Ruta para eliminar una orden
    path("gestionarOrden/", views.inicio_vista, name="gestionarOrden")
]
