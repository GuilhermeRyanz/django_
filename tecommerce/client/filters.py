from django_filters import rest_framework as filters

from client import models

class ClientFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr='exact')

    class Meta:
        model = models.Client
        fields = ['name', 'age']