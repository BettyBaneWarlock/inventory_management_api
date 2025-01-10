from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import InventoryItemViewSet

router = DefaultRouter()
router.register(r'inventory-items', InventoryItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # include the API URLs
    path('api-token-auth/', views.obtain_auth_token),  # include the API token authentication URL
]
