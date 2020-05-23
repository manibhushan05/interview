from django.db import models
from djmoney.models.fields import MoneyField


class State(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2, unique=True)


class City(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)


class Address(models.Model):
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100, default='')
    line3 = models.CharField(max_length=100, default='')
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Bank(models.Model):
    name = models.CharField(max_length=70, default='')
    code = models.CharField(max_length=3, unique=True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)


class Branch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    ifsc = models.CharField(max_length=11)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)


class Customer(models.Model):
    class Status(models.IntegerChoices):
        ACTIVE = 0
        BLOCKED = 1
        BANNED = 2
        COMPROMISED = 3
        ARCHIVED = 4
        CLOSED = 5
        UNKNOWN = 6

    status = models.IntegerField(choices=Status.choices)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, null=True)
    phone = models.CharField(max_length=10)


class AccountType(models.Model):
    withdraw_limit = MoneyField(max_digits=14, decimal_places=2, default_currency='INR')


class Account(models.Model):
    class Status(models.IntegerChoices):
        ACTIVE = 0
        BLOCKED = 1
        BANNED = 2
        COMPROMISED = 3
        ARCHIVED = 4
        CLOSED = 5
        UNKNOWN = 6

    status = models.IntegerField(choices=Status.choices)
    account_number = models.CharField(max_length=25)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='INR')
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='INR')


class Card(models.Model):
    CATEGORY_CHOICES = (
        ('DC', 'Debit Card'),
        ('CC', 'Credit Card'),
        ('CH', 'Cash Card'),
    )

    class Status(models.IntegerChoices):
        ACTIVE = 0
        BLOCKED = 1
        BANNED = 2
        COMPROMISED = 3
        ARCHIVED = 4
        CLOSED = 5
        UNKNOWN = 6

    status = models.IntegerField(choices=Status.choices)
    card_number = models.CharField(max_length=16)
    category = models.CharField(max_length=2)
    cvv = models.CharField(max_length=4)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    card_holder = models.ForeignKey(to=Account, on_delete=models.DO_NOTHING)


class Atm(models.Model):
    code = models.CharField(max_length=10)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)


class AtmHardware(models.Model):
    code = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    atm = models.ForeignKey(Atm, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class CashDispenser(AtmHardware):
    pass


class Screen(AtmHardware):
    pass


class Keypad(AtmHardware):
    pass


class Printer(AtmHardware):
    pass


class CardReader(AtmHardware):
    pass


class DepositSlot(AtmHardware):
    pass


class CheckDepositSlot(AtmHardware):
    pass


class Transaction(models.Model):
    class Status(models.IntegerChoices):
        SUCCESS = 0
        FAILURE = 1
        BLOCKED = 2
        FULL = 3
        PARTIAL = 4
        NONE = 5

    transaction_id = models.CharField(max_length=30)
    status = models.IntegerField(choices=Status.choices, default=Status.SUCCESS)
    created_at = models.DateField(auto_now=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    atm = models.ForeignKey(Atm, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class BalanceEnquiry(Transaction):
    pass


class Deposit(Transaction):
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='INR')


class Withdraw(Transaction):
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='INR')


class Transfer(Transaction):
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='INR')
    from_account = models.ForeignKey(Account, related_name='from_account_transfer', on_delete=models.CASCADE)
    to_account = models.ForeignKey(Account, related_name='to_account_transfer', on_delete=models.CASCADE)
