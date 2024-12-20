# Generated by Django 3.1.3 on 2024-11-19 17:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20241119_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.IntegerField()),
                ('p_name', models.CharField(max_length=50)),
                ('p_image', models.ImageField(upload_to='product_images/')),
                ('cost', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='cert_reg_img',
            field=models.ImageField(null=True, upload_to='cert_reg/'),
        ),
        migrations.CreateModel(
            name='Uploaded_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(default=datetime.datetime(2024, 11, 19, 17, 53, 7, 852270, tzinfo=utc))),
                ('updated_date', models.DateField(default=datetime.datetime(2024, 11, 19, 17, 53, 7, 852270, tzinfo=utc))),
                ('pid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.product')),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Buy_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_date', models.DateField(default=datetime.datetime(2024, 11, 19, 17, 53, 7, 852270, tzinfo=utc))),
                ('buyer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer', to='webapp.user')),
                ('pid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.product')),
                ('seller_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seller', to='webapp.user')),
            ],
        ),
    ]
