# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-01 12:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uinfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='afflition',
            new_name='organization',
        ),
    ]
