# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 06:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20170326_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='gender',
        ),
    ]
