from django.db import models

from common.models import Location
from driver.models import Driver
from common.models import AuditLog


class Vehicle(AuditLog):
    vehicle_number = models.CharField(max_length=12)


class VehicleDriver(AuditLog):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)


class Cab(Vehicle):
    class Category(models.IntegerChoices):
        PREMIER = 0
        UBER_GO = 1

    category = models.IntegerField(choices=Category.choices)


class Bike(Vehicle):
    class Category(models.IntegerChoices):
        PREMIER = 0
        UBER_GO = 1

    category = models.IntegerField(choices=Category.choices)


# need to be discussed
class VehicleLocation(Location):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
