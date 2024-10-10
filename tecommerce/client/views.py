from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination

from client import models, serializers, pagination


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    # pagination_class = pagination.ClientPagination
    permission_classes = (permissions.IsAuthenticated,)
