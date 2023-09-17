from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer_name = models.CharField(max_length=255)
    booking_date = models.DateField()
    num_guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.customer_name} - {self.booking_date}"
