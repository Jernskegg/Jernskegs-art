# Generated by Django 3.2 on 2022-03-29 00:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageentry',
            name='water_marked_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='water_marked_image'),
        ),
    ]
