# Generated by Django 5.0.7 on 2024-08-04 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olcha_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 8, 4, 10, 58, 50, 835703, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
