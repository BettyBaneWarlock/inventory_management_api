from rest_framework import serializers
from inventory.models import InventoryItem

# Define a serializer for the InventoryItem model
class InventoryItemSerializer(serializers.ModelSerializer):
    # Metadata about the serializer
    class Meta:
        # Specify the model to be serialized
        model = InventoryItem
        # Define the fields that will be included in the serialized output
        fields = ['id', 'name', 'description', 'quantity', 'price', 'category', 'date_created']

    # Custom method to handle object creation
    def create(self, validated_data):
        # Automatically set the 'user' field to the currently authenticated user
        user = self.context['request'].user
        validated_data['user'] = user  # Assign the authenticated user to the 'user' field
        # Call the superclass's create method with the updated validated data
        return super().create(validated_data)
