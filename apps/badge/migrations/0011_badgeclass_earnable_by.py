# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badge', '0010_auto_20161112_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='badgeclass',
            name='earnable_by',
            field=models.CharField(choices=[('earner', 'earner'), ('moderator', 'moderator')], default='earner', max_length=10),
        ),
    ]
