# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 02:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bestbud', '0003_purchase_numberid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='numberid',
        ),
    ]