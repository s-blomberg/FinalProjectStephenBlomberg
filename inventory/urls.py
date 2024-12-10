from django.urls import path
from .views import InventoryListView, InventoryCreateView, InventoryUpdateView, home, InventoryDeleteView, InventoryDetailView, delete_image

urlpatterns = [
    path('', home, name='home'),
    path('list/', InventoryListView.as_view(), name='inventory_list'),
    path('add/', InventoryCreateView.as_view(), name='add_inventory_item'),
    path('edit/<int:pk>/', InventoryUpdateView.as_view(), name='edit_inventory_item'),
    path('delete/<int:pk>/', InventoryDeleteView.as_view(), name='delete_inventory_item'),
    path('details/<int:pk>/', InventoryDetailView.as_view(), name='inventory_detail'),
    path('delete-image/<int:pk>/', delete_image, name='delete_image'),
]
