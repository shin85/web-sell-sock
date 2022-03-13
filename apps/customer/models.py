from django.db import models

# Create your models here.
class Customer(models.Model):
    class Meta:
        verbose_name = 'Khách hàng'
        verbose_name_plural = 'Khách hàng'
    
    def __str__(self):
        return self.username
    
    username = models.CharField(max_length=200, null=False, blank=False, verbose_name='Tài khoản')
    email = models.EmailField(max_length=200, null=False)
    password = models.CharField(max_length=50, default="",blank=True, null=True, verbose_name='Mật khẩu')
    salt = models.CharField(max_length=20, default="",blank=True, null=True)
    balance = models.IntegerField(default=0, verbose_name='Số dư')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Tạo lúc')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Cập nhật lúc')
    

class History(models.Model):
    class Meta:
        verbose_name = 'Lịch sử'
        verbose_name_plural='Lịch sử'
    
    def __str__(self):
        return self.customer
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Khách hàng')
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Mô tả')
    balance_change = models.IntegerField(default=0, verbose_name='Số tiền')
    balance_after = models.IntegerField(default=0, verbose_name='Số dư sau')
    balance_before = models.IntegerField(default=0, verbose_name='Số dư trước')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Tạo lúc')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Cập nhật lúc')

    # define a method save history
    def save_history(customer, description, balance_change, balance_after, balance_before):
        history = History()
        history.customer = customer
        history.description = description
        history.balance_change = balance_change
        history.balance_after = balance_after
        history.balance_before = balance_before
        history.save()