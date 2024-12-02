from django import forms
from .models import InventoryItem

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = '__all__'
        widgets = {
            'date_acquired': forms.DateInput(attrs={'type': 'date'}),
            'date_maintenance': forms.DateInput(attrs={'type': 'date'}),
        }
