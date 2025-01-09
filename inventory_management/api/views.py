from rest_framework import viewsets
from inventory.models import InventoryItem
from .serializers import InventoryItemSerializer
from rest_framework.permissions import IsAuthenticated

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def get_queryset(self):
        # Ensure users only access their own inventory items
        return InventoryItem.objects.filter(user=self.request.user)
