from django import forms
from .models import MaintenanceLog

class MaintenanceLogForm(forms.ModelForm):
    class Meta:
        model = MaintenanceLog
        fields = ['last_maintenance_date', 'light_bulb_hours', 'serial_id', 'product_model', 'ballast_unit', 'notes']
        widgets = {
            'last_maintenance_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
