# Generated by Django 3.2.2 on 2021-05-18 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0004_commission_item_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commission',
            name='item_info',
        ),
    ]
