from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class AuditLog(models.Model):
    created_at = models.DateTimeField(
        'Created at',
        auto_now_add=True,
        db_index=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Created by',
        blank=True, null=True,
        related_name="%(app_label)s_%(class)s_created_by",
        on_delete=models.SET_NULL)
    last_modified_at = models.DateTimeField(
        'Last modified at',
        auto_now=True,
        db_index=True)
    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Last modified by',
        blank=True, null=True,
        related_name="%(app_label)s_%(class)s_last_modified_by",
        on_delete=models.SET_NULL)

    deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class ContactBook(AuditLog):
    name = models.CharField(max_length=255, unique=True, db_index=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Contact(AuditLog):
    name = models.CharField(max_length=255, db_index=True)  # accepts UTF-8
    email = models.EmailField(max_length=254, db_index=True)  # As described in RFC3696 Errata ID 1690
    contact_book = models.ForeignKey(to=ContactBook, on_delete=models.CASCADE, related_name='contacts')

    class Meta:
        ordering = ('-id',)
        # considering same email in two or more contactbook but unique within contact book
        unique_together = ('contact_book', 'email')

    def __str__(self):
        return self.email
