from django.contrib import admin
from .models import MaintenanceLog

@admin.register(MaintenanceLog)
class MaintenanceLogAdmin(admin.ModelAdmin):
    list_display = ('last_maintenance_date', 'light_bulb_hours', 'ballast_unit')
    search_fields = ('ballast_unit',)
