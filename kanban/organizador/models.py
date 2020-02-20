from django.db import models

# Create your models here.
class Tablero(models.Model):
    creartablero = models.CharField(max_length=30)
    def __str__(self):
        return self.creartablero

class Lista(models.Model):
    nombreLista = models.CharField(max_length=30)
    fkTablero= models.ForeignKey(Tablero, on_delete = models.CASCADE,related_name="listas")
    def __str__(self):
        return self.nombreLista
    
class Tarea(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    fkLista = models.ForeignKey(Lista, on_delete = models.CASCADE, related_name="tareas")
    def __str__(self):
        return self.nombre
