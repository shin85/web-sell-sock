# Generated by Django 3.2.12 on 2022-02-26 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socks',
            old_name='Node',
            new_name='node',
        ),
    ]
