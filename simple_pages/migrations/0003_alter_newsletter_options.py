# Generated by Django 3.2 on 2022-04-20 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_pages', '0002_newsletter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name': 'Newsletter Email Address', 'verbose_name_plural': 'Newsletter Email Addresses'},
        ),
    ]
