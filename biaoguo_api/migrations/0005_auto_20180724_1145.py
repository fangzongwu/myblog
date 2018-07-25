# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-07-24 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biaoguo_api', '0004_auto_20180706_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='is_commend',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]