# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-18 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmoni', '0015_auto_20180518_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domainname',
            name='cert_valid_days',
            field=models.IntegerField(default=None, null=True),
        ),
    ]