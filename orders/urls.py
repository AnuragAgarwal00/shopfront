from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('admin/order/<int:order_id>/', views.order_admin_detail, name='order_admin_detail'),
    path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),
    
]
