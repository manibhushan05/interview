from django.db import models

from utils.common_model import AuditLog


class Location(models.Model):
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lng = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    location_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    address = models.CharField(max_length=255, null=True)


class Vehicle(AuditLog):
    vehicle_number = models.CharField(max_length=12)


class Cab(Vehicle):
    class Category(models.IntegerChoices):
        PREMIER = 0
        UBER_GO = 1

    category = models.IntegerField(choices=Category.choices)


# need to be discussed
class VehicleLocation(Location):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
