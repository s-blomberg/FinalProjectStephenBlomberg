from django.contrib import admin
from .models import InventoryItem

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'serial_id', 'cost', 'quantity', 'date_acquired', 'date_maintenance')
    list_filter = ('date_acquired', 'date_maintenance')
    search_fields = ('product_name', 'serial_id')
