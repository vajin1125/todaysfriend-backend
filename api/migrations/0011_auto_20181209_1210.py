# Generated by Django 2.1.3 on 2018-12-09 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_product_pdu_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pdu_recommended',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pdu_show_tourpage',
            field=models.IntegerField(null=True),
        ),
    ]
