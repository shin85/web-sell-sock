from django.db import models

# Create your models here.
class Order(models.Model):
    class Meta:
        verbose_name='Đơn hàng'
        verbose_name_plural='Đơn hàng'
        
    plan_id = models.ForeignKey('plan.Plan', on_delete=models.SET_NULL, null=True, verbose_name='Gói Sock')
    customer_id = models.ForeignKey('customer.Customer', verbose_name='Khách hàng', on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField(verbose_name='Số lượng', default=1, null=False, blank=False)
    price_total = models.IntegerField(verbose_name='Tổng tiền', null=False, blank=False)
    balance_after = models.IntegerField(verbose_name='Số dư sau khi mua', null=False, blank=False)
    balance_before = models.IntegerField(verbose_name='Số dư trước khi mua', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)