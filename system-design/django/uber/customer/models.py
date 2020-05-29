from django.conf import settings
from django.db import models

from common.models import AuditLog


class Customer(AuditLog):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True, db_index=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name
