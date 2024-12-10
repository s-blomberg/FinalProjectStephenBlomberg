from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import MaintenanceLogForm
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SpotlightMaintenanceForm, GeneralEquipmentMaintenanceForm
from .models import MaintenanceLog, InventoryItem
from inventory.forms import InventoryItemForm
from django.contrib import messages

# Create Maintenance Log
class MaintenanceLogCreateView(CreateView):
    model = MaintenanceLog
    form_class = MaintenanceLogForm
    template_name = 'maintenance_logs/add_maintenance_log.html'

    def form_valid(self, form):
        inventory_item = get_object_or_404(InventoryItem, id=self.kwargs['pk'])
        form.instance.inventory_item = inventory_item
        form.save()
        return redirect('inventory_detail', pk=inventory_item.id)


class MaintenanceLogUpdateView(UpdateView):
    model = MaintenanceLog
    form_class = MaintenanceLogForm
    template_name = 'maintenance_logs/edit_maintenance_log.html'

    def get_success_url(self):
        return reverse_lazy('inventory_detail', kwargs={'pk': self.object.inventory_item.id})


class MaintenanceLogDeleteView(DeleteView):
    model = MaintenanceLog
    template_name = 'maintenance_logs/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('inventory_detail', kwargs={'pk': self.object.inventory_item.id})


def add_maintenance_log(request, pk, form_type=None):
    # Get the inventory item
    inventory_item = get_object_or_404(InventoryItem, pk=pk)

    # Determine the form type
    if form_type == "spotlight":
        form_class = SpotlightMaintenanceForm
    elif form_type == "general":
        form_class = GeneralEquipmentMaintenanceForm
    else:
        # Redirect if no valid form type is specified
        return redirect('inventory_detail', pk=inventory_item.id)

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            maintenance_log = form.save(commit=False)
            maintenance_log.inventory_item = inventory_item
            maintenance_log.save()
            return redirect('inventory_detail', pk=inventory_item.id)
    else:
        form = form_class()

    return render(request, 'maintenance_logs/add_maintenance_log.html', {
        'form': form,
        'inventory_item': inventory_item,
        'form_type': form_type,
    })

def edit_inventory_item(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)

    if request.method == "POST":
        form = InventoryItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Inventory item updated successfully!")
            return redirect("inventory_detail", pk=item.id)
        else:
            messages.error(request, "Error updating inventory item.")
    else:
        form = InventoryItemForm(instance=item)

    return render(request, "edit_inventory_item.html", {"form": form, "object": item})