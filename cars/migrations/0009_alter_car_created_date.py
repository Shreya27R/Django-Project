# Generated by Django 4.1 on 2022-11-06 09:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_alter_car_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 11, 6, 9, 49, 35, 821379, tzinfo=datetime.timezone.utc)),
        ),
    ]
