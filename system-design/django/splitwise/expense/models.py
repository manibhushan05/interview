from django.conf import settings
from django.db import models
from djmoney.forms import MoneyField


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


class Expense(AuditLog):
    amount = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='INR')
    description = models.CharField(max_length=255, default='')
    date = models.DateField()
    category = models.CharField(max_length=10,default='')
    status = models.BooleanField(default=True)


class ExpenseUser(AuditLog):
    paid_share = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='INR')
    owed_share = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='INR')
    net_balance = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='INR')
    user = models.ForeignKey(related_name='expense_user', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Debt(AuditLog):
    amount = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='INR')
    payer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='debt_payer', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='debt_receiver', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
