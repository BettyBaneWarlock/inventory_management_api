from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import InventoryItem, Category

# Form for user registration, extending the default UserCreationForm
class UserRegisterForm(UserCreationForm):
    # Add an email field with validation for user registration
    email = forms.EmailField()

    # Specify metadata for the form
    class Meta:
        # Define the model this form interacts with (User model)
        model = User
        # Fields to include in the form
        fields = ['username', 'email', 'password1', 'password2']

# Form for creating or updating inventory items
class InventoryItemForm(forms.ModelForm):
    # Dropdown field to select a category, with all categories as options
    category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)

    # Specify metadata for the form
    class Meta:
        # Define the model this form interacts with (InventoryItem model)
        model = InventoryItem
        # Fields to include in the form
        fields = ['name', 'description', 'quantity', 'price', 'category']
