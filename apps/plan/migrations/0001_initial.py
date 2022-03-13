# Generated by Django 3.2.12 on 2022-02-26 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tên gói')),
                ('price', models.IntegerField(verbose_name='Giá')),
                ('description', models.TextField(verbose_name='Mô tả')),
                ('duration', models.IntegerField(verbose_name='Thời gian sử dụng')),
                ('time_min', models.IntegerField(verbose_name='Sử dụng tối thiểu')),
                ('active', models.BooleanField(default=True, verbose_name='Kích hoạt')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Gói Sock',
                'verbose_name_plural': 'Gói Sock',
            },
        ),
    ]
