# Generated by Django 5.1.4 on 2025-02-01 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes/'),
        ),
        migrations.AddField(
            model_name='qrcode',
            name='name',
            field=models.CharField(default='fdf', max_length=255),
            preserve_default=False,
        ),
    ]
