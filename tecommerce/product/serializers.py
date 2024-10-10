from rest_framework import serializers
from product import models


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = 'id', 'description', 'quantity', 'dt_modified', 'cs_active'