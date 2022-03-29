# Generated by Django 3.2 on 2022-03-28 23:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='CommissionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PEND', 'Pending'), ('ORDR', 'Ordered'), ('URWE', 'Under Review'), ('ACPD', 'Accepted'), ('DECL', 'Declined'), ('IPRR', 'In progress'), ('DONE', 'Done'), ('USRW', 'User review')], default='PEND', max_length=4)),
                ('image_size', models.CharField(choices=[('X256', '256 x 256'), ('X512', '512 x 512'), ('TX1K', '1024 x 1024'), ('TX2K', '2048 x 2048'), ('L108', '1080p (Landscape)'), ('P108', '1080p (Portrait)'), ('LA2k', '2k (Landscape)'), ('PO2K', '2k (Portait)'), ('LA4K', '4k (Landscape)'), ('PO4k', '4K (Portrait)')], max_length=4)),
                ('user_description', models.TextField()),
                ('date_requested', models.DateTimeField(auto_now=True)),
                ('requested_by', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=models.SET('Deleted Genre'), to='commission.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('comment_content', models.TextField(max_length=255)),
                ('comment_atached_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='commission.commissionrequest')),
                ('comment_posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]
