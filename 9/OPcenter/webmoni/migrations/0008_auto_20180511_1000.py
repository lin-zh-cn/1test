# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-11 10:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webmoni', '0007_auto_20180511_0959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domainname',
            old_name='check',
            new_name='check_id',
        ),
    ]