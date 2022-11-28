# Generated by Django 2.1.3 on 2018-11-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdu_name', models.CharField(max_length=200)),
                ('pdu_type', models.CharField(max_length=200)),
                ('pdu_country', models.CharField(max_length=200)),
                ('pdu_city', models.CharField(max_length=200)),
                ('pdu_language', models.CharField(max_length=200)),
                ('pdu_brief_description', models.TextField(blank=True, null=True)),
                ('pdu_detailed_description', models.TextField(blank=True, null=True)),
                ('pdu_hashtag', models.CharField(max_length=600)),
                ('pdu_meeting_time', models.TimeField(blank=True, null=True)),
                ('pdu_duration', models.TimeField(blank=True, null=True)),
                ('pdu_location', models.CharField(max_length=600)),
                ('pdu_hottoget', models.TextField(blank=True, null=True)),
                ('pdu_price', models.IntegerField(default=0)),
                ('pdu_price_include', models.CharField(max_length=600)),
                ('pdu_min_guest', models.IntegerField(default=0)),
                ('pdu_max_guest', models.IntegerField(default=0)),
                ('pdu_season_from', models.DateField(blank=True, null=True)),
                ('pdu_season_to', models.DateField(blank=True, null=True)),
                ('pdu_unavailable_date', models.DateField()),
                ('pdu_additional_info', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
