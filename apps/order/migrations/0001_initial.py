# Generated by Django 3.2.12 on 2022-02-27 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plan', '0003_auto_20220226_2110'),
        ('customer', '0007_customer_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1, verbose_name='Số lượng')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer', verbose_name='Khách hàng')),
                ('plan_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plan.plan', verbose_name='Gói Sock')),
            ],
            options={
                'verbose_name': 'Đơn hàng',
                'verbose_name_plural': 'Đơn hàng',
            },
        ),
    ]
