from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_inventory_item, name='add_inventory_item'),
    path('edit/<int:pk>/', views.edit_inventory_item, name='edit_inventory_item'),
]
