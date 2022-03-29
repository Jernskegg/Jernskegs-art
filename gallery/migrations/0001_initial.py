# Generated by Django 3.2 on 2022-03-28 23:55

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('water_marked_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product entries',
                'ordering': ['-date_posted'],
            },
        ),
    ]
