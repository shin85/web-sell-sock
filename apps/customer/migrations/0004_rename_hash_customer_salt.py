# Generated by Django 3.2.12 on 2022-02-22 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_customer_hash'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='hash',
            new_name='salt',
        ),
    ]