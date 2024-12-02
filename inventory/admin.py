from django.contrib import admin
from .models import InventoryItem

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'serial_id', 'cost', 'quantity', 'date_acquired', 'date_maintenance')
    list_filter = ('date_acquired', 'date_maintenance')
    search_fields = ('product_name', 'serial_id')

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
