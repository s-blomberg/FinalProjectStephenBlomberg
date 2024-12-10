from django import forms
from .models import MaintenanceLog

class MaintenanceLogForm(forms.ModelForm):
    class Meta:
        model = MaintenanceLog
        fields = ['last_maintenance_date', 'notes']
        widgets = {
            'last_maintenance_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class SpotlightMaintenanceForm(forms.ModelForm):
    class Meta:
        model = MaintenanceLog
        fields = ['last_maintenance_date', 'light_bulb_hours', 'ballast_unit', 'notes']
        widgets = {
            'last_maintenance_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'light_bulb_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'ballast_unit': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class GeneralEquipmentMaintenanceForm(forms.ModelForm):
    class Meta:
        model = MaintenanceLog
        fields = ['last_maintenance_date', 'work_performed', 'parts_replaced', 'notes']
        widgets = {
            'last_maintenance_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'work_performed': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe the work performed'}),
            'parts_replaced': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'List parts replaced'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }