# Generated by Django 3.2 on 2022-03-31 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20220329_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageorderinfo',
            name='client_id',
            field=models.CharField(default='', max_length=255),
        ),
    ]
