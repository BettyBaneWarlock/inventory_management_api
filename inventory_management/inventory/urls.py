from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, Dashboard, AddItem, EditItem, DeleteItem
from django.contrib.auth import views as auth_views

# URL patterns for the application
urlpatterns = [
    # Home page route, handled by the Index view
    path('', Index.as_view(), name='index'),

    # Dashboard route, handled by the Dashboard view
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

    # Route for adding a new inventory item, handled by the AddItem view
    path('add-item/', AddItem.as_view(), name='add-item'),

    # Route for editing an inventory item, using the item's primary key (pk)
    # Handled by the EditItem view
    path('edit-item/<int:pk>/', EditItem.as_view(), name='edit-item'),

    # Route for deleting an inventory item, using the item's primary key (pk)
    # Handled by the DeleteItem view
    path('delete-item/<int:pk>/', DeleteItem.as_view(), name='delete-item'),

    # Route for user signup, handled by the SignUpView
    path('signup/', SignUpView.as_view(), name='signup'),

    # Route for user login, using Django's built-in LoginView
    # Specifies a custom template for the login page
    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),

    # Route for user logout, using Django's built-in LogoutView
    # Specifies a custom template for the logout confirmation page
    path('logout/', auth_views.LogoutView.as_view(template_name='inventory/logout.html'), name='logout'),
]
