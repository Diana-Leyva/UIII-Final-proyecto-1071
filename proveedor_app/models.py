from django.db import models

class Proveedor(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=100)
    correo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    paginaweb = models.CharField(max_length=100)
    TIPO_CHOICES = [
        (1, 'Fabricante'),
        (2, 'Mayorista'),
        (3, 'Menudista'),
    ]
    tipo = models.IntegerField(choices=TIPO_CHOICES)
    
    def __str__(self):
        return self.nombre


"""
    codigo = 
    nombre = 
    telefono =
    correo = 
    direccion = 
    paginaweb = 
    tipo = 
"""