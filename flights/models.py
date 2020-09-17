from django.db import models

# Create your models here.
class Airport(models.Model):

    code = models.CharField(max_length=3)
    city = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    # origin = models.CharField(max_length = 64)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    # cascade - means to delete corespondig flights, to prevent, models.protect
    # related name: this is to map te relationship backwards, if I have an airport what are it's destinations
    # take a flight.origin and get the airport (origin), but if I have an airport how do I get the flights
    # that are set as that origin, related name builds that
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self): #string representation
        return f"{self.id}: {self.origin} to {self.destination}"

    def is_valid_flight(self):
        return self.origin != self.destination or self.duration >= 0

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True,related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
