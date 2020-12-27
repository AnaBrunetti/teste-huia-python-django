from django.contrib import admin
from .models import (
    Client,
    QualityLot,
    Product,
    Order
)

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'birth_date', 'inactive']
    search_fields = ['name', 'cpf', 'birth_date', 'inactive']
    ordering = ['name'] 


@admin.register(QualityLot)
class QualityLotAdmin(admin.ModelAdmin):
    list_display = ['id', 'fabrication_date', 'quality', 'inactive']
    search_fields = ['id', 'fabrication_date', 'quality', 'inactive']
    ordering = ['-fabrication_date']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'color', 'price', 'inactive']
    search_fields = ['name', 'description', 'color', 'price', 'inactive']
    ordering = ['name'] 


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_value', 'purchase_date', 'inactive']
    search_fields = ['id', 'total_value', 'purchase_date', 'inactive']
    filter_horizontal = ['products']
    ordering = ['-id']           
