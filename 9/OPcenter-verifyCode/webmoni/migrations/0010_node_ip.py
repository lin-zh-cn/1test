# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-16 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmoni', '0009_auto_20180514_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='ip',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
