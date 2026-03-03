from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'staff', 'total_amount', 'discount_percent', 'final_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at', 'staff']
    search_fields = ['order_number', 'staff__username']
    inlines = [OrderItemInline]
    readonly_fields = ['created_at', 'updated_at']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'item', 'quantity', 'price', 'subtotal']
    list_filter = ['order__status']