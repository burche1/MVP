# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestbud', '0005_purchase_compra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='compra',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date purchased'),
        ),
    ]