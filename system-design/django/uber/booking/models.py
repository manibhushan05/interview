from django.db import models

from customer.models import Customer
from driver.models import Driver
from utils.common_model import AuditLog, Location


class Ride(AuditLog):
    class Status(models.IntegerChoices):
        PENDING = 0
        APPROVED = 1
        REJECTED = 2
        START = 3
        PARTIAL = 4
        EXPIRED = 6

    driver = models.ForeignKey(Driver, null=True, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Driver, null=True, on_delete=models.CASCADE)
    sharable = models.BooleanField()
    status = models.IntegerField(choices=Status.choices, default=Status.PENDING)


class Booking(AuditLog):
    class Status(models.IntegerChoices):
        PENDING = 0
        APPROVED = 1
        REJECTED = 2
        START = 3
        PARTIAL = 4
        COMPLETED = 5
        EXPIRED = 6

    start_location = models.ForeignKey(Location, related_name='booking_start_locations', on_delete=models.SET_NULL)
    end_location = models.ForeignKey(Location, related_name='booking_end_locations', on_delete=models.SET_NULL)
    vehicle_arrival_time = models.DateTimeField(null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    expiry_time = models.DateTimeField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices, default=Status.PENDING)
