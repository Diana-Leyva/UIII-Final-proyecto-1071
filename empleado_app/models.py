from django.db import models

class Empleado(models.Model):
    idempleado = models.CharField(primary_key=True, max_length=6)
    idsucursal = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=100)
    correo = models.CharField(max_length=20)
    turno = models.CharField(max_length=20)
    posicion = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre



"""
    codigo =
    nombre = 
    telefono = 
    direccion = 
    correo = 
    turno =
    posicion =
"""