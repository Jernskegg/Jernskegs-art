# Generated by Django 3.2 on 2022-03-29 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20220329_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageorderinfo',
            name='order_total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=32),
        ),
    ]
