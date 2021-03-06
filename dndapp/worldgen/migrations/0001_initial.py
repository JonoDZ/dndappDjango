# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appearance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Appearance', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Name_first_female',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Name_first_male',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Name_last',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Personailty1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personailty', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Personailty2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personailty', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='name_last',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.Race'),
        ),
        migrations.AddField(
            model_name='name_first_male',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.Race'),
        ),
        migrations.AddField(
            model_name='name_first_female',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.Race'),
        ),
    ]
