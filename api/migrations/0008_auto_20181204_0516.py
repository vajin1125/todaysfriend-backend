# Generated by Django 2.1.3 on 2018-12-03 19:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_productimage_pdu_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pdu_ustr',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productimage',
            name='pdu_ustr',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productimage',
            name='pdu_img_url',
            field=models.FileField(upload_to='static/uploads/images/'),
        ),
    ]
