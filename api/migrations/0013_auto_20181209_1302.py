# Generated by Django 2.1.3 on 2018-12-09 03:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20181209_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='city_img_bar',
            new_name='city_img_bar_url',
        ),
        migrations.AddField(
            model_name='city',
            name='city_image_bar_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
