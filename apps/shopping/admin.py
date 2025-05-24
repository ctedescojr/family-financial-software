from django.contrib import admin
from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("id", "vehicle_name", "fuel", "fuel_price")
    list_filter = ["fuel"]
    search_fields = ["vehicle_name"]
