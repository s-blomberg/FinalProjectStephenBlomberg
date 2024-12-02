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
    def clean_serial_id(self):
        serial_id = self.cleaned_data.get('serial_id')
        if InventoryItem.objects.filter(serial_id=serial_id).exists():
            raise forms.ValidationError("An inventory item with this Serial ID already exists.")
        return serial_id
