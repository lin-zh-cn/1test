# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-24 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20180524_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='no_login',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
