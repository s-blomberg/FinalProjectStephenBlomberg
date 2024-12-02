from django.urls import path
from .views import InventoryListView, InventoryCreateView, InventoryUpdateView, home

urlpatterns = [
    path('', home, name='home'),
    path('list/', InventoryListView.as_view(), name='inventory_list'),
    path('add/', InventoryCreateView.as_view(), name='add_inventory_item'),
    path('edit/<int:pk>/', InventoryUpdateView.as_view(), name='edit_inventory_item'),
]
