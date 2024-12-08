from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import InventoryItem
from .forms import InventoryItemForm
from django.db.models import Q

# 'Home' view after login
def home(request):
    return render(request, 'inventory/home.html')

# View item list
class InventoryListView(ListView):
    model = InventoryItem
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'inventory_items'

    def get_queryset(self):
        queryset = InventoryItem.objects.only(
            'id', 'product_name', 'date_maintenance', 'notes'
        )

        # Handle search
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(product_name__icontains=query) |
                Q(notes__icontains=query)
            )

        # Handle sorting
        sort = self.request.GET.get('sort')
        if sort:
            queryset = queryset.order_by(sort)

        return queryset


# View item details
class InventoryDetailView(DetailView):
    model = InventoryItem
    template_name = 'inventory/inventory_detail.html'
    context_object_name = 'item'

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

# Delete inventory item
class InventoryDeleteView(DeleteView):
    model = InventoryItem
    template_name = 'inventory/confirm_delete.html'
    success_url = reverse_lazy('inventory_list')