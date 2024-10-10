from rest_framework import viewsets, permissions
from sale.models import Sale
from sale import serializers


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = serializers.SaleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)