# Generated by Django 3.2.12 on 2022-02-26 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Mô tả'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='duration',
            field=models.IntegerField(default=0, verbose_name='Thời gian sử dụng'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='price',
            field=models.IntegerField(default=10000, verbose_name='Giá'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='time_min',
            field=models.IntegerField(default=10, verbose_name='Sử dụng tối thiểu'),
        ),
    ]
