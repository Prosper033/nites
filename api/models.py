from django.db import models

# Create your models here.


class Aircraft(models.Model):
    aircraft_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.aircraft_number}: {self.name}\t{self.type}\t{self.capacity}'


class Flight(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.RESTRICT)
    flight_number = models.CharField(max_length=50, unique=True)
    take_off_point = models.CharField(max_length=150)
    take_off_time = models.DateTimeField()
    destination = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=18, decimal_places=4)
    flight_class = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.aircraft}\t{self.flight_number}\t{self.take_off_point}\t{self.take_off_time}\t{self.destination}\t{self.price}\t{self.flight_class}'


class Passenger(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}\t{self.phone}\t{self.address}\t{self.email}'


class Booking(models.Model):
    Flight = models.ForeignKey(Flight, on_delete=models.RESTRICT)
    Passenger = models.ForeignKey(Passenger, on_delete=models.RESTRICT)
    booking_reference = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=18, decimal_places=4)
    take_off_point = models.CharField(max_length=150)
    take_off_time = models.DateTimeField()
    destination = models.CharField(max_length=150)
    flight_class = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.booking_reference}\t{self.price}\t{self.take_off_point}{self.take_off_time}\t{self.destination}\t{self.flight_class}'
