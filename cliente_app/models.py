from django.db import models

class Cliente(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)  
    nombre = models.CharField(max_length=20)  
    telefono = models.CharField(max_length=10)  
    direccion = models.CharField(max_length=100)  
    correo = models.EmailField(max_length=100)  
    fnacimiento = models.DateField() 
    fregistro = models.DateField() 

    def __str__(self):
        return self.nombre


"""
    codigo =
    nombre = 
    telefono = 
    direccion = 
    correo = 
    fnacimiento =
    fregistro =
"""