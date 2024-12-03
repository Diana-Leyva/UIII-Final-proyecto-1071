from django.db import models

class Empleado(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=20)
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