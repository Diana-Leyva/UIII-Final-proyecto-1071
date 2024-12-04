from django.db import models

class Producto(models.Model):
    idproducto = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=20)
    idsucursal = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20)
    idproveedor = models.CharField(max_length=20)
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