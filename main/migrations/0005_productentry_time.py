# Generated by Django 5.1 on 2024-09-16 18:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_product_productentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='productentry',
            name='time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
