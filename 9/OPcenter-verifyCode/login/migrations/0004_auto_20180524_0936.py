# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-24 09:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_login_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login_User',
            new_name='User',
        ),
    ]