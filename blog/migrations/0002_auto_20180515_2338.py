# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-15 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-create_time']},
        ),
    ]
