# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldgen', '0013_auto_20170416_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item_gear',
            old_name='cost',
            new_name='costCopper',
        ),
        migrations.RenameField(
            model_name='item_weapon',
            old_name='cost',
            new_name='costCopper',
        ),
        migrations.AddField(
            model_name='item_gear',
            name='costGold',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item_gear',
            name='costSilver',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item_weapon',
            name='costGold',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item_weapon',
            name='costSilver',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
