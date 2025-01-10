from django.db import models
from django.contrib.auth.models import User

# Model to represent an inventory item
class InventoryItem(models.Model):
    # Name of the inventory item
    name = models.CharField(max_length=200)
    
    # Detailed description of the inventory item
    description = models.TextField()
    
    # Quantity of the item in stock
    quantity = models.IntegerField()
    
    # Price of the item, allowing up to 10 digits with 2 decimal places
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Category the item belongs to; optional field
    category = models.ForeignKey(
        'Category',  # References the Category model
        on_delete=models.SET_NULL,  # Sets category to NULL if the category is deleted
        blank=True,  # Allows this field to be blank
        null=True    # Allows this field to store NULL in the database
    )
    
    # Timestamp for when the item was created
    date_created = models.DateTimeField(auto_now_add=True)
    
    # User who added or owns the inventory item
    user = models.ForeignKey(
        User,  # References the built-in User model
        on_delete=models.CASCADE  # Deletes the inventory item if the user is deleted
    )

    # String representation of the model for readability
    def __str__(self):
        return self.name

# Model to represent categories for inventory items
class Category(models.Model):
    # Name of the category
    name = models.CharField(max_length=200)

    # Metadata for the model
    class Meta:
        verbose_name_plural = 'categories'  # Displays "categories" in plural form in the admin panel

    # String representation of the model for readability
    def __str__(self):
        return self.name
