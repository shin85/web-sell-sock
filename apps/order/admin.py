from django.contrib import admin
from .models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def id_display(self, obj):
        return "Đơn hàng "+ str(obj.id)
    id_display.short_description = "Đơn hàng"
    def plan_display(self, obj):
        return obj.plan_id.name
    plan_display.short_description = "Gói Sock"
    def price_display(self, obj):
        return '{:,}'.format(obj.plan_id.price)
    price_display.short_description = "Giá"
    def price_total_display(self, obj):
        return '{:,}'.format(obj.price_total)
    price_total_display.short_description = "Tổng tiền"
    def balance_before_display(self, obj):
        return '{:,}'.format(obj.balance_before)
    balance_before_display.short_description = "Số dư trước khi mua"
    def balance_after_display(self, obj):
        return '{:,}'.format(obj.balance_after)
    balance_after_display.short_description = "Số dư sau khi mua"
    
    list_display = ('id_display', 'customer_id', 'plan_display', 'price_display', 'amount', 'price_total_display', 'balance_before_display', 'balance_after_display', 'created_at')
    list_display_links = None
    
    # Search by customer_id
    search_fields = ['customer_id__username', 'plan_id__name']
    
    # Filter by customer_id
    list_filter = ('customer_id', 'plan_id__name',)
    
    # Sort by created_at
    ordering = ('-created_at',)
    
    # Show 10 items per page
    list_per_page = 20
    
    # Disable add new
    def has_add_permission(self, request):
        return False
    
    # Disable delete
    def has_delete_permission(self, request, obj=None):
        return False