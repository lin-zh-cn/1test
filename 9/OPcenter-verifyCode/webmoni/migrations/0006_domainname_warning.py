# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-11 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmoni', '0005_auto_20180509_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='domainname',
            name='warning',
            field=models.IntegerField(default=0),
        ),
    ]
