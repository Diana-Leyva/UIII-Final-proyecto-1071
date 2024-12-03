from django.db import models

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20)
    proveedor = models.CharField(max_length=20)
    total = models.PositiveSmallIntegerField()
    stock = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre

"""
    codigo = 
    nombre =
    descripcion = 
    categoria =
    proveedor = 
    total = 
    stock =
"""