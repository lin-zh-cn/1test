# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-26 14:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='online',
            new_name='online_status',
        ),
    ]