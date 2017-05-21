# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParkYamManagerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_clean',
            field=models.BooleanField(default=True, verbose_name='Clean'),
        ),
        migrations.AlterField(
            model_name='room',
            name='bathroom_type',
            field=models.IntegerField(choices=[(0, 'Bathtub'), (1, 'Shower')], default='Shower', verbose_name='Bathroom Type'),
        ),
    ]
