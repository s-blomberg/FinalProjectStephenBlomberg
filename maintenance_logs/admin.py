from django.contrib import admin
from .models import MaintenanceLog

@admin.register(MaintenanceLog)
class MaintenanceLogAdmin(admin.ModelAdmin):
    list_display = ('serial_id', 'last_maintenance_date', 'light_bulb_hours', 'product_model', 'ballast_unit')
    search_fields = ('serial_id', 'product_model', 'ballast_unit')
