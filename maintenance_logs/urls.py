from django.urls import path
from . import views

urlpatterns = [
    path('', views.maintenance_list, name='maintenance_list'),
    path('<int:pk>/', views.MaintenanceLogDetailView.as_view(), name='maintenance_detail'),
    path('add/', views.add_maintenance_log, name='add_maintenance_log'),
    path('add/<int:inventory_item_id>/', views.add_maintenance_log, name='add_maintenance_log_for_item'),
]
