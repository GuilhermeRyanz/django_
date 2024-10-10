from rest_framework import viewsets, permissions
from client import models, serializers


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = (permissions.IsAuthenticated,)