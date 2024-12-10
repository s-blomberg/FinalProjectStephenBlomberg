from django.urls import path
from .views import (
    MaintenanceLogCreateView, MaintenanceLogUpdateView, MaintenanceLogDeleteView, add_maintenance_log
)

urlpatterns = [
    path('inventory/<int:pk>/maintenance/add/', MaintenanceLogCreateView.as_view(), name='add_maintenance_log'),
    path('maintenance/edit/<int:pk>/', MaintenanceLogUpdateView.as_view(), name='edit_maintenance_log'),
    path('maintenance/delete/<int:pk>/', MaintenanceLogDeleteView.as_view(), name='delete_maintenance_log'),
    path('inventory/<int:pk>/maintenance/add/<str:form_type>/', add_maintenance_log, name='add_maintenance_log'),
]
