# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-24 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_remove_user_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='no_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_pw',
        ),
    ]
