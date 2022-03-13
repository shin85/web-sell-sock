from django.db import models

# Create your models here.
class Plan(models.Model):
    class Meta:
        verbose_name='Gói Sock'
        verbose_name_plural='Gói Sock'
        
    name = models.CharField(max_length=100, verbose_name='Tên gói', null=False, blank=False)
    price = models.IntegerField(verbose_name='Giá', default=10000, null=False, blank=False)
    description = models.TextField(verbose_name='Mô tả', null=True, blank=True)
    duration = models.IntegerField(verbose_name='Thời gian sử dụng (phút)', default=0, null=False, blank=False)
    time_min = models.IntegerField(verbose_name='Sử dụng tối thiểu (phút)', default=10, null=False, blank=False)
    active = models.BooleanField(default=True, verbose_name='Kích hoạt')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

