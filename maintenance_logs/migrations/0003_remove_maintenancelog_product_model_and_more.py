# Generated by Django 5.1.3 on 2024-12-10 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_inventoryitem_product_image'),
        ('maintenance_logs', '0002_maintenancelog_inventory_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenancelog',
            name='product_model',
        ),
        migrations.RemoveField(
            model_name='maintenancelog',
            name='serial_id',
        ),
        migrations.AddField(
            model_name='maintenancelog',
            name='parts_replaced',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='maintenancelog',
            name='work_performed',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maintenancelog',
            name='inventory_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_logs', to='inventory.inventoryitem'),
        ),
    ]