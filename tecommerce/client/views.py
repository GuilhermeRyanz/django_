from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from client import models, serializers, pagination, filters


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    filter_backends = (DjangoFilterBackend,)
    filtersets_class = filters.ClientFilter
    # pagination_class = pagination.ClientPagination
    permission_classes = (permissions.IsAuthenticated,)

