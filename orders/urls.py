from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='orders-welcome'),
    path('admin-orders/', views.adminOrders, name='admin-orders'),
    path('driver-orders/', views.driverOrders, name='driver-orders'),

    path('order-create/', views.orderCreate, name='order-create'),
    path('order-details/<str:pk>/', views.orderDetails, name='order-details'),
    path('order-update/<str:pk>', views.orderUpdate, name="order-update"),
    path('order-delete/<str:pk>', views.orderDelete, name="order-delete"),


]
