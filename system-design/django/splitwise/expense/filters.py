from django_filters import rest_framework as filters

from expense.models import Expense, Repayment, ExpenseUser


class ExpenseFilter(filters.FilterSet):
    id = filters.CharFilter(field_name="id", label="id", lookup_expr='exact')

    class Meta:
        model = Expense
        fields = ['id', ]


class ExpenseUserFilter(filters.FilterSet):
    id = filters.CharFilter(field_name="id", label="id", lookup_expr='exact')

    class Meta:
        model = ExpenseUser
        fields = ['id', ]


class RepaymentFilter(filters.FilterSet):
    id = filters.CharFilter(field_name="id", label="id", lookup_expr='exact')

    class Meta:
        model = Repayment
        fields = ['id', ]
