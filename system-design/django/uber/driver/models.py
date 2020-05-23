from django.conf import settings
from django.db import models

from utils.common_model import AuditLog


class Driver(AuditLog):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True, db_index=True)
    dl_number = models.CharField(max_length=25, null=True, unique=True)
    dl_validity = models.DateField(null=True)
