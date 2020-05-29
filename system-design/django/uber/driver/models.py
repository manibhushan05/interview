from django.conf import settings
from django.db import models

from common.models import AuditLog


class Driver(AuditLog):
    class Status(models.IntegerChoices):
        pending = 0
        verified = 1
        rejected = 2
        banned = 3
        idle = 4
        driving = 5
        inactive = 6

    status = models.IntegerField(choices=Status.choices)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True, db_index=True)
    dl_number = models.CharField(max_length=25, null=True, unique=True)
    dl_validity = models.DateField(null=True)
