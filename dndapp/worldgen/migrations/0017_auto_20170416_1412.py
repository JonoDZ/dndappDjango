# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldgen', '0016_auto_20170416_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_weapon',
            name='costCopper',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item_weapon',
            name='costGold',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item_weapon',
            name='costSilver',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item_weapon',
            name='damageDieQuant',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item_weapon',
            name='damageDieType',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item_weapon',
            name='weaponRangeMax',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item_weapon',
            name='weaponRangeMin',
            field=models.IntegerField(default=0),
        ),
    ]
