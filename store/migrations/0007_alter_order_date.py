# Generated by Django 3.2.4 on 2021-07-08 08:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20210703_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 8, 30, 24, 335839, tzinfo=utc)),
        ),
    ]
