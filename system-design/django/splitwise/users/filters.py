from django_filters import rest_framework as filters

from users.models import CustomUser


class CustomUserFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name="first_name", label="First Name", lookup_expr='iexact')
    email = filters.CharFilter(field_name="email", label="First Name", lookup_expr='iexact')

    class Meta:
        model = CustomUser
        fields = ['first_name', ]
