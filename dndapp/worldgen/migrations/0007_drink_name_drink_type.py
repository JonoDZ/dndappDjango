# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-08 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldgen', '0006_auto_20170312_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drinkName', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Drink_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drinkType', models.CharField(max_length=20)),
            ],
        ),
    ]
