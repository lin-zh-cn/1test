# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-09 11:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webmoni', '0003_auto_20180509_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domainname',
            old_name='check',
            new_name='check_id',
        ),
    ]