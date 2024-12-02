from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import InventoryItem
from .forms import InventoryItemForm

# Updated 'home' view
def home(request):
    return render(request, 'inventory/home.html')

# View-only list for all users
class InventoryListView(ListView):
    model = InventoryItem
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'inventory_items'

# Add new inventory items (Admins only)
class InventoryCreateView(PermissionRequiredMixin, CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/add_inventory_item.html'
    permission_required = 'inventory.add_inventoryitem'
    success_url = reverse_lazy('inventory_list')

    def form_invalid(self, form):
        messages.error(self.request, "There was an error adding the inventory item.")
        print(form.errors)  # Log form errors for debugging
        return super().form_invalid(form)

# Edit inventory items (Admins only)
class InventoryUpdateView(PermissionRequiredMixin, UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/edit_inventory_item.html'
    permission_required = 'inventory.change_inventoryitem'

    def get_success_url(self):
        return reverse_lazy('inventory_list')

class InventoryDeleteView(DeleteView):
    model = InventoryItem
    template_name = 'inventory/confirm_delete.html'
    success_url = reverse_lazy('inventory_list')