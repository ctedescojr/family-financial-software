from django.db import models
from shopping.choices import Fuel


class Vehicle(models.Model):
    class Meta:
        proxy = True  # Tells Djan go that this is a "mirror" model
        verbose_name = "01 - Veículo"
        verbose_name_plural = "01 - Veículoss"

    vehicle_name = models.CharField(max_lenght=150)

    fuel = models.CharField(
        max_length=1,
        choices=Fuel.choices,
        default=Fuel.NONE,
        verbose_name="Combustível",
    )
    fuel_price = models.DecimalField(max_digits=10, decimal_places=2)


class Invoice(models.Model):
    image = models.ImageField(upload_to="invoices/")
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    detected_on = models.DateTimeField(auto_now_add=True)
