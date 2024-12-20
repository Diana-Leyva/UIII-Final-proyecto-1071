from django.db import models

class Sucursal(models.Model):
    idsucursal = models.CharField(primary_key=True, max_length=6)  
    nombre = models.CharField(max_length=100)  
    correo = models.EmailField(max_length=100) 
    gerente = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)  
    telefono = models.CharField(max_length=15) 
    horario = models.CharField(max_length=50)  

    def __str__(self):
        return self.nombre
