# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestbud', '0020_auto_20171117_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='product',
        ),
        migrations.AddField(
            model_name='purchase',
            name='name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='purchase',
            name='totalprice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]