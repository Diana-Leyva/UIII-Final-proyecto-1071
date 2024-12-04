from django.db import models

class Orden(models.Model):
    idorden = models.CharField(primary_key=True, max_length=6)  # Código único de la orden
    idcliente = models.CharField(max_length=20)  # Nombre del cliente que realiza la orden
    idempleado = models.CharField(max_length=20)  # Dirección de entrega
    idsucursal = models.CharField(max_length=20)
    idproducto = models.CharField(max_length=20)
    forden = models.DateField() 
    total = models.PositiveSmallIntegerField()  # Monto total de la orden

    def __str__(self):
        return f"Orden de {self.cliente} - {self.codigo}"
