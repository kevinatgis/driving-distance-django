# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 12:43
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dd_node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnt', models.IntegerField(null=True)),
                ('chk', models.IntegerField(null=True)),
                ('ein', models.IntegerField(null=True)),
                ('eout', models.IntegerField(null=True)),
                ('seq', models.IntegerField(null=True)),
                ('node', models.BigIntegerField(null=True)),
                ('edge', models.BigIntegerField(null=True)),
                ('cost', models.FloatField(null=True)),
                ('agg_cost', models.FloatField(null=True)),
                ('the_geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='dd_poly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pgr_pointsaspolygon', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
            ],
        ),
    ]
