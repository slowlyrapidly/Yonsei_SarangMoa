# Generated by Django 3.1.3 on 2024-11-24 21:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20241125_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy_list',
            name='buy_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 24, 21, 42, 12, 6884, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='uploaded_product',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 24, 21, 42, 12, 6884, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='uploaded_product',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 24, 21, 42, 12, 6884, tzinfo=utc)),
        ),
    ]