# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-17 04:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0004_auto_20171017_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard_news',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
