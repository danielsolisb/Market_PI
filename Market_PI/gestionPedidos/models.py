from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Su Nombre')
    direccion = models.CharField(max_length=50, verbose_name='Dirección')
    email = models.EmailField(blank=True, null=True)
    tfno = models.CharField(max_length=15)
    #para mostrar campos, no se puede mostrar mas de un campo
    #si se desea puede revisar en admin.py la clase creada para elloS
    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()



