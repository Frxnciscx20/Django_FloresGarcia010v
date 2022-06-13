from django.db import models

# Create your models here.


class Producto(models.Model):
    idPro=models.IntegerField(primary_key=True, verbose_name='Idproducto')
    nombre=models.CharField(max_length=50, verbose_name='Nombre')
    marca= models.CharField(max_length=20, verbose_name='Marca')
    precio= models.IntegerField(max_length=6, verbose_name='Precio')
    imagen=models.ImageField(upload_to="producto", null=True)

    def __str__(self):
        return self.idPro


class Cliente(models.Model):
    rut = models.CharField(max_length=6, primary_key=True, verbose_name='rut')
    nombre = models.CharField(max_length=20, verbose_name='nombre')
    apellido=models.CharField(max_length=20, verbose_name='informacion')
    

    def __str__(self):
        return self.rut
