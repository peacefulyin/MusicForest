# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0004_auto_20170914_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='album',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]