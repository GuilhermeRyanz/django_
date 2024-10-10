from rest_framework import viewsets, permissions
from employee import serializers
from employee.models import Employee


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
