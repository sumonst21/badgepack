# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 16:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_auto_20161022_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='accepted_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_accepted_by', to=settings.AUTH_USER_MODEL),
        ),
    ]