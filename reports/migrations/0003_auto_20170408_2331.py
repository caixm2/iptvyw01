# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 23:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_tztesheji'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thwsheji',
            old_name='podid',
            new_name='popid',
        ),
    ]
