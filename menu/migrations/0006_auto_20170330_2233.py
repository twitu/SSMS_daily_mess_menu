# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20170330_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Meal'),
        ),
    ]
