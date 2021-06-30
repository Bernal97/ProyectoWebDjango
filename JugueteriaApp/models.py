from django.db import models

# Create your models here.
class Categoria (models.Model):
    nombreCate = models.CharField(max_length=20)
    def __str__(self):
        return self.nombreCate
    

class Producto (models.Model):
    nombre = models.CharField(max_length = 50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre
    


