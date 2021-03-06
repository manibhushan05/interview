from django.conf import settings
from django.db import models


class Location(models.Model):
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lng = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    location_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    address = models.CharField(max_length=255, null=True)


class AuditLog(models.Model):
    created_at = models.DateTimeField(
        'Created at',
        auto_now_add=True,
        db_index=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Created by',
        null=True,
        related_name="%(app_label)s_%(class)s_created_by",
        on_delete=models.SET_NULL)
    last_modified_at = models.DateTimeField(
        'Last modified at',
        auto_now=True,
        db_index=True)
    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Last modified by',
        null=True,
        related_name="%(app_label)s_%(class)s_last_modified_by",
        on_delete=models.SET_NULL)

    deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
