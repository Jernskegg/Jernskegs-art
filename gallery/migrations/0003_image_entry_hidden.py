# Generated by Django 3.2 on 2022-03-09 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_image_entry_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_entry',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
