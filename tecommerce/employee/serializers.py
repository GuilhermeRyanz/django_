from rest_framework import serializers
from employee import models

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Employee
        fields = 'id', 'name', 'registraction', 'dt_modified', 'cs_active'