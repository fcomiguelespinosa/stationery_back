from .models import Sale
from .serializers import SaleSerializer
from rest_framework import viewsets
from rest_framework import permissions


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [permissions.IsAuthenticated]
