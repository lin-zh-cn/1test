# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-17 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmoni', '0013_auto_20180517_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domainname',
            name='cert_valid_days',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
