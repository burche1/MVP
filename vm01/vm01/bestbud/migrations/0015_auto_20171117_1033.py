# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestbud', '0014_product_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='logo',
            field=models.ImageField(upload_to='bestbud/static/images'),
        ),
    ]
