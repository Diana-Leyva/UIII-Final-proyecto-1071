from django.db import models

class Orden(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)  # Código único de la orden
    cliente = models.CharField(max_length=20)  # Nombre del cliente que realiza la orden
    direccion = models.CharField(max_length=100)  # Dirección de entrega
    
    # Estado de la orden
    ESTADO_CHOICES = [
        (1, 'Procesando'),
        (2, 'Enviando'),
        (3, 'En entrega'),
    ]
    estado = models.IntegerField(choices=ESTADO_CHOICES)

    # Fecha de la orden
    forden = models.DateField() 
    
    # Total de la orden
    total = models.PositiveSmallIntegerField()  # Monto total de la orden
    
    # Método de pago
    METODO_PAGO_CHOICES = [
        (1, 'Tarjeta'),
        (2, 'Efectivo'),
        (3, 'Credito'),
    ]
    metodo_pago = models.IntegerField(choices=METODO_PAGO_CHOICES)

    def __str__(self):
        return f"Orden de {self.cliente} - {self.codigo}"
