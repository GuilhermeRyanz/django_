from rest_framework import serializers
from client import models

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Client
        fields = ['id', 'name', 'age', 'rg', 'cpf', 'dt_modified', 'cs_active']
