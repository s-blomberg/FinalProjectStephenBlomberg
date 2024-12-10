from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import InventoryItem
from .forms import InventoryItemForm
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse

# Home View
def home(request):
    return render(request, 'inventory/home.html')

# View Inventory List
class InventoryListView(ListView):
    model = InventoryItem
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'inventory_items'
    paginate_by = 10

    def get_queryset(self):
        queryset = InventoryItem.objects.only(
            'id', 'product_name', 'date_maintenance', 'notes', 'product_image'
        )
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(product_name__icontains=query) |
                Q(notes__icontains=query)
            )
        sort = self.request.GET.get('sort')
        if sort:
            queryset = queryset.order_by(sort)
        return queryset

# View Inventory Details
class InventoryDetailView(DetailView):
    model = InventoryItem
    template_name = 'inventory/inventory_detail.html'
    context_object_name = 'item'

# Create Inventory Item
class InventoryCreateView(PermissionRequiredMixin, CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/add_inventory_item.html'
    permission_required = 'inventory.add_inventoryitem'
    success_url = reverse_lazy('inventory_list')

    def form_valid(self, form):
        messages.success(self.request, "Inventory item added successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error adding the inventory item.")
        print(form.errors)  # Log errors for debugging
        return super().form_invalid(form)

# Update Inventory Item
class InventoryUpdateView(PermissionRequiredMixin, UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/edit_inventory_item.html'
    permission_required = 'inventory.change_inventoryitem'
    success_url = reverse_lazy('inventory_list')

    def form_valid(self, form):
        if form.cleaned_data['product_image'] and old_image:
            old_image.delete(save=False)

        form.save()
        messages.success(self.request, "Inventory item updated successfully.")
        return super().form_valid(form)

# Delete Inventory Item
class InventoryDeleteView(DeleteView):
    model = InventoryItem
    template_name = 'inventory/confirm_delete.html'
    success_url = reverse_lazy('inventory_list')
    success_message = 'Inventory item deleted successfully.'

def delete_image(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    if item.product_image:
        item.product_image.delete(save=False)
        item.save()
        messages.success(request, "Image deleted successfully.")
    else:
        messages.error(request, "No image to delete.")
    return HttpResponseRedirect(reverse('edit_inventory_item', args=[pk]))
