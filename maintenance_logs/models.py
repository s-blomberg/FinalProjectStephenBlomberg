from django.db import models
from inventory.models import InventoryItem

class MaintenanceLog(models.Model):
    inventory_item = models.ForeignKey(
        InventoryItem,
        on_delete=models.CASCADE,
        related_name='maintenance_logs',
    )
    last_maintenance_date = models.DateField(null=True, blank=True)
    light_bulb_hours = models.IntegerField(null=True, blank=True)
    ballast_unit = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    work_performed = models.TextField(blank=True, null=True)
    parts_replaced = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Log for {self.inventory_item or 'Unassigned'} - {self.last_maintenance_date or 'No Date'}"
