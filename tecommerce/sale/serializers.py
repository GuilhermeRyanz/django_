from rest_framework import serializers
from sale import models

class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sale
        fields = ['id', 'nrf', 'dt_modified', 'cs_active', 'id_employee', 'id_product', 'id_client']
