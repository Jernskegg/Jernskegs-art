# Generated by Django 3.2 on 2022-03-09 10:34

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image_entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('image', cloudinary.models.CloudinaryField(default='no-image', max_length=255, verbose_name='image')),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]