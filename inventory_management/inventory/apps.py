from django.apps import AppConfig

# Define the configuration for the "inventory" app
class InventoryConfig(AppConfig):
    # Specify the default auto field for model primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Define the name of the app as 'inventory'
    name = 'inventory'

    # Override the ready method to perform initialization tasks when the app is loaded
    def ready(self):
        # Import signals for the inventory app
        # This ensures the signal handlers are connected when the app is ready
        import inventory.signals
