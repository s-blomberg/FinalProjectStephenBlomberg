from django import forms
from .models import InventoryItem

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = '__all__'
        widgets = {
            'date_acquired': forms.DateInput(attrs={'type': 'date'}),
            'date_maintenance': forms.DateInput(attrs={'type': 'date'}),
            'product_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_serial_id(self):
        serial_id = self.cleaned_data.get('serial_id')

        # Check if serial_id is duplicate
        existing_item = InventoryItem.objects.filter(serial_id=serial_id).exclude(pk=self.instance.pk).first()
        if existing_item:
            raise forms.ValidationError("An inventory item with this Serial ID already exists.")

        return serial_id