from django.db import models

class InventoryItem(models.Model):
    product_name = models.CharField(max_length=255, verbose_name="Product Name")
    serial_id = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name="Serial ID")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cost")
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    date_acquired = models.DateField(verbose_name="Date Acquired")
    date_maintenance = models.DateField(verbose_name="Date of Maintenance", null=True, blank=True)
    notes = models.TextField(blank=True, verbose_name="Notes")
    product_image = models.ImageField(upload_to='inventory_images/', blank=True, null=True, verbose_name="Product Image")

    def __str__(self):
        return f"{self.product_name} ({self.serial_id})"
