# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestbud', '0002_auto_20171117_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='numberid',
            field=models.IntegerField(default=0),
        ),
    ]
