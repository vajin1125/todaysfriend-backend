# Generated by Django 2.1.3 on 2018-12-02 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_productimage_pdu_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='pdu_uid',
        ),
    ]
