# Generated by Django 3.1.3 on 2024-11-12 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20241112_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=20)),
                ('pw', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('birth', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('address', models.CharField(max_length=20)),
                ('authorization', models.IntegerField(null=True)),
            ],
        ),
    ]
