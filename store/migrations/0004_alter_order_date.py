# Generated by Django 3.2.4 on 2021-07-03 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 3, 19, 37, 22, 708555)),
        ),
    ]
