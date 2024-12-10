from django.shortcuts import render, get_object_or_404, redirect
from inventory.models import InventoryItem
from django.views.generic import ListView, DetailView
from .models import MaintenanceLog
from .forms import MaintenanceLogForm

def maintenance_list(request):
    logs = MaintenanceLog.objects.all()
    return render(request, 'maintenance_logs/maintenance_list.html', {'logs': logs})

class MaintenanceLogListView(ListView):
    model = MaintenanceLog
    template_name = 'maintenance_logs/maintenance_list.html'
    context_object_name = 'maintenance_logs'
    paginate_by = 10

    def get_queryset(self):
        return MaintenanceLog.objects.select_related('inventory_item').all()

class MaintenanceLogDetailView(DetailView):
    model = MaintenanceLog
    template_name = 'maintenance_logs/maintenance_detail.html'
    context_object_name = 'log'

def add_maintenance_log(request, inventory_item_id=None):
    inventory_item = None
    if inventory_item_id:
        inventory_item = get_object_or_404(InventoryItem, id=inventory_item_id)

    if request.method == 'POST':
        form = MaintenanceLogForm(request.POST)
        if form.is_valid():
            maintenance_log = form.save(commit=False)
            if inventory_item:
                maintenance_log.inventory_item = inventory_item
            maintenance_log.save()
            return redirect('maintenance_list')
    else:
        form = MaintenanceLogForm(initial={'inventory_item': inventory_item})

    return render(request, 'maintenance_logs/add_maintenance_log.html', {'form': form, 'inventory_item': inventory_item})
