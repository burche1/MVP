# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestbud', '0016_auto_20171117_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='logo',
            field=models.ImageField(upload_to='images'),
        ),
    ]