# Generated by Django 3.2 on 2022-03-29 03:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageorderinfo',
            name='user',
            field=models.ForeignKey(blank=True, default=0, on_delete=models.SET(0), to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requestorderinfo',
            name='user',
            field=models.ForeignKey(blank=True, default=0, on_delete=models.SET(0), to='auth.user'),
            preserve_default=False,
        ),
    ]
