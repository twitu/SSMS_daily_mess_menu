# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meal', models.CharField(choices=[('gr', 'GRUB'), ('ln', 'LUNCH'), ('din', 'DINNER'), ('br', 'BREAKFAST')], max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.meal'),
        ),
    ]