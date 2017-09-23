# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 05:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0003_auto_20170912_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('stars', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='sheet',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='piano.Album'),
        ),
    ]
