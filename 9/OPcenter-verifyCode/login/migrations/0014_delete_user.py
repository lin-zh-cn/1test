# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-24 13:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_auto_20180524_1312'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
