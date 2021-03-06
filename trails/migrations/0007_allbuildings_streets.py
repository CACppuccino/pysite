# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-14 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0006_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allbuildings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primarykey', models.TextField(blank=True, db_column='PrimaryKey', null=True, unique=True)),
                ('streetname', models.TextField(blank=True, db_column='StreetName', null=True)),
                ('streetno', models.FloatField(blank=True, db_column='StreetNo', null=True)),
                ('buildingname', models.TextField(blank=True, db_column='BuildingName', null=True)),
                ('buildingpix', models.TextField(blank=True, db_column='BuildingPix', null=True)),
                ('pixcaption', models.TextField(blank=True, db_column='PixCaption', null=True)),
                ('builddate', models.TextField(blank=True, db_column='BuildDate', null=True)),
                ('demolishdate', models.TextField(blank=True, db_column='DemolishDate', null=True)),
                ('architect', models.TextField(blank=True, db_column='Architect', null=True)),
                ('builder', models.TextField(blank=True, db_column='Builder', null=True)),
                ('info', models.TextField(blank=True, db_column='Info', null=True)),
                ('links', models.TextField(blank=True, db_column='Links', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'AllBuildings',
            },
        ),
        migrations.CreateModel(
            name='Streets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, db_column='Name', null=True, unique=True)),
                ('link', models.TextField(blank=True, db_column='Link', null=True)),
                ('streetpix', models.TextField(blank=True, db_column='StreetPix', null=True)),
                ('streetpix_caption', models.TextField(blank=True, db_column='StreetPix Caption', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Streets',
            },
        ),
    ]
