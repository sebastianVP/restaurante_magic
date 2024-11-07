from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Nombre del cliente
    email = models.EmailField()
    date = models.DateTimeField()  # Fecha y hora de la reserva
    guests = models.IntegerField()  # Cantidad de invitados

    def __str__(self):
        return f"Reserva en {self.restaurant} para {self.name}"
