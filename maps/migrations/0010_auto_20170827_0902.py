# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0009_auto_20170825_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dd_poly',
            name='session',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]