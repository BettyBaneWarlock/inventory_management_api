from django.contrib import admin
from .models import InventoryItem, Category

# Register the InventoryItem model with the admin site
# This allows InventoryItem objects to be managed through the Django admin interface
admin.site.register(InventoryItem)

# Register the Category model with the admin site
# This enables management of categories through the Django admin interface
admin.site.register(Category)
