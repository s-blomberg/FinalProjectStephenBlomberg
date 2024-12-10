# Generated by Django 5.1.3 on 2024-12-10 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_inventoryitem_product_image'),
        ('maintenance_logs', '0005_alter_maintenancelog_inventory_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancelog',
            name='inventory_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_logs', to='inventory.inventoryitem'),
        ),
    ]
