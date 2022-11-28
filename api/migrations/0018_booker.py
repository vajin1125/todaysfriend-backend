# Generated by Django 2.1.3 on 2018-12-13 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20181212_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fristname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('ages', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=600)),
                ('email', models.EmailField(max_length=200)),
                ('bookingDate', models.DateField(blank=True, null=True)),
                ('cellNumber', models.CharField(max_length=200)),
                ('mainSNS', models.CharField(max_length=200, null=True)),
                ('snsId', models.CharField(max_length=200, null=True)),
                ('numberPeople', models.IntegerField(default=0)),
                ('someNote', models.TextField(null=True)),
            ],
        ),
    ]
