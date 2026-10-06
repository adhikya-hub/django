import django_filters
from django.db.models.expressions import field_types

from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(
        field_name="emp_designation", lookup_expr="iexact"
    )

    class Meta:
        model = Employee
        fields = ["designation"]
