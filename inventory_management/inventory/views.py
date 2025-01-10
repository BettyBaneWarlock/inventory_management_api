from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, InventoryItemForm
from .models import InventoryItem, Category
from inventory_management.settings import LOW_QUANTITY
from django.contrib import messages

# Home page view
class Index(TemplateView):
    template_name = 'inventory/index.html'  # Specifies the template for the home page

# Dashboard view, requiring the user to be logged in
class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        # Fetch all inventory items associated with the logged-in user
        items = InventoryItem.objects.filter(user=self.request.user.id).order_by('id')

        # Fetch items with low inventory based on the defined threshold
        low_inventory = InventoryItem.objects.filter(
            user=self.request.user.id,
            quantity__lte=LOW_QUANTITY
        )

        # Display a message if there are items with low inventory
        if low_inventory.count() > 0:
            if low_inventory.count() > 1:
                messages.error(request, f'{low_inventory.count()} items have low inventory')
            else:
                messages.error(request, f'{low_inventory.count()} item has low inventory')

        # Get the IDs of items with low inventory for highlighting
        low_inventory_ids = InventoryItem.objects.filter(
            user=self.request.user.id,
            quantity__lte=LOW_QUANTITY
        ).values_list('id', flat=True)

        # Render the dashboard with all items and low inventory highlights
        return render(request, 'inventory/dashboard.html', {'items': items, 'low_inventory_ids': low_inventory_ids})

# User signup view
class SignUpView(View):
    def get(self, request):
        # Render the signup form on a GET request
        form = UserRegisterForm()
        return render(request, 'inventory/signup.html', {'form': form})
        
    def post(self, request):
        # Process the submitted form on a POST request
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            # Save the user and log them in
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('index')  # Redirect to the home page on successful signup

        # Re-render the form with errors if it is invalid
        return render(request, 'inventory/signup.html', {'form': form})

# View for adding a new inventory item
class AddItem(LoginRequiredMixin, CreateView):
    model = InventoryItem  # Specify the model to be used
    form_class = InventoryItemForm  # Use the inventory item form
    template_name = 'inventory/item_form.html'  # Template for the add item page
    success_url = reverse_lazy('dashboard')  # Redirect to dashboard after adding an item

    def get_context_data(self, **kwargs):
        # Add category options to the form context
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        # Automatically associate the item with the currently logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)

# View for editing an existing inventory item
class EditItem(LoginRequiredMixin, UpdateView):
    model = InventoryItem  # Specify the model to be updated
    form_class = InventoryItemForm  # Use the inventory item form
    template_name = 'inventory/item_form.html'  # Template for editing an item
    success_url = reverse_lazy('dashboard')  # Redirect to dashboard after editing an item

# View for deleting an inventory item
class DeleteItem(LoginRequiredMixin, DeleteView):
    model = InventoryItem  # Specify the model to be deleted
    template_name = 'inventory/delete_item.html'  # Template for confirming deletion
    success_url = reverse_lazy('dashboard')  # Redirect to dashboard after deleting an item
    context_object_name = 'item'  # Context variable name for the item in the template
