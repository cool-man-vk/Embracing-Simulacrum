# Generated by Django 3.2.2 on 2021-05-18 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0003_auto_20210518_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='item_info',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='auction_app.item'),
        ),
    ]
