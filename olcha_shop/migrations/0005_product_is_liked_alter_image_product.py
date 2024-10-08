# Generated by Django 5.0.7 on 2024-08-08 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olcha_shop', '0004_alter_attribute_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='olcha_shop.product'),
        ),
    ]
