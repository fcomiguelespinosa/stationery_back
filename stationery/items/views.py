from .models import Item
from .serializers import ItemSerializer
from rest_framework import viewsets
from rest_framework import permissions


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
