from rest_framework import serializers
from inventory.models import InventoryItem

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'description', 'quantity', 'price', 'category', 'date_created']

    def create(self, validated_data):
        # Automatically set the user to the currently authenticated user
        user = self.context['request'].user
        validated_data['user'] = user  # Automatically set the user
        return super().create(validated_data)
