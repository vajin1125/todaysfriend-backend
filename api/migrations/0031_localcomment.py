# Generated by Django 2.1.3 on 2018-12-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_eventcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('comment', models.TextField(blank=True)),
                ('lastUpdated', models.DateTimeField(blank=True)),
                ('articleId', models.IntegerField(default=0)),
                ('parentId', models.IntegerField(default=0)),
            ],
        ),
    ]
