# Generated by Django 5.1.6 on 2025-03-04 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentcars', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
    ]
