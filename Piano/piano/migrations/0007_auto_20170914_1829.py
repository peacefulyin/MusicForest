# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0006_auto_20170914_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='\u7434\u53cb', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='uname',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]