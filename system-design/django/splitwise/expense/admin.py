from django.contrib import admin

from expense.models import Expense, ExpenseUser, Repayment

admin.site.register(Expense)
admin.site.register(ExpenseUser)
admin.site.register(Repayment)
