# Generated by Django 2.1.3 on 2018-11-23 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pdu_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 24, 3, 31, 24, 319035)),
        ),
    ]
