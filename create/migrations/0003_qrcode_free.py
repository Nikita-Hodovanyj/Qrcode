# Generated by Django 5.1.4 on 2025-02-21 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0002_qrcode_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='free',
            field=models.BooleanField(default=False),
        ),
    ]
