# Generated by Django 5.1.4 on 2025-02-07 23:22

import create.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0002_qrcode_image_qrcode_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2024-02-08 12:00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=create.models.user_directory_path),
        ),
    ]
